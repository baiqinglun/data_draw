import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
import json
from tqdm import tqdm
from tool import get_paths, voltage_to_pressure_factor
import csv
from matplotlib import rcParams
from Colors import Color

# 合成输出文件全名
def getOutputFilename(image_name):
    return os.path.basename(image_name).split(".")[0] + ".png"

# 一次性读取所有文件并绘图
class CurveManager:
    def __init__(self, file_list=None):
        # 读取配置文件
        with open('settings/curve_settings.json', 'r', encoding='UTF-8') as settings_file:
            settings_data = dict(json.load(settings_file))
            self.uni_data = settings_data["uni_data"]
            self.file_names = settings_data["file_names"]
            self.data = settings_data["data"]
            self.deal = settings_data["deal"]
            self.max_pressure_rise_start = self.deal["max_pressure_rise_start"]
            self.max_pressure_rise_end = self.deal["max_pressure_rise_end"]
            self.font = settings_data["font"]
            self.grid = settings_data["grid"]
            self.line = settings_data["line"]
            self.title = settings_data["title"]
            self.lengend = settings_data["lengend"]
            self.xy_label = settings_data["xy_label"]
            self.tick_param = settings_data["tick_param"]
            self.spines = settings_data["spines"]
            self.image = settings_data["image"]
            self.text = settings_data["text"]
            self.colors = Color["more"][1]
            
            # 中文使用宋体，英文使用新罗马字体
            config = {
                "font.family":'serif',
                "mathtext.fontset":'stix',
                "font.serif": 'timessimsun',
                "font.weight":'bold',
                "font.size":self.font["font_size"]
            }
            rcParams.update(config)
            plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题
            
        # 创建输出文件夹
        if self.image["output_folder"] and not os.path.exists(self.image["output_folder"]):
            os.makedirs(self.image["output_folder"])

    # 循环所有csv数据文件，开始处理
    def Run(self):
        for one_data in self.uni_data:
            self.ResetParams()
            self.GetOneData(one_data)
            self.file_list = os.listdir(os.path.join(os.getcwd(), "data/"+self.data_folder))
            self.file_list.sort(key=lambda x:x.split('-')[1]) if self.is_gas else self.file_list.sort(key=lambda x:int(x.split('-')[1]))

            if (len(self.file_names) == 0):
                self.mass_list = [file.split('-')[1].split(".")[0] for file in self.file_list if file.endswith('.CSV') or file.endswith('.csv')]
                self.lengend_list = [file.split('-')[1] for file in self.file_list if file.endswith('.CSV') or file.endswith('.csv')]
                self.file_names = [file.split('-')[1]+'-'+file.split('-')[2]+'-'+file.split('-')[3]+"-"+file.split('-')[4] for file in self.file_list if file.endswith('.CSV') or file.endswith('.csv')]
                self.file_count += sum(1 for file in self.file_list if file.endswith(".CSV") or file.endswith('.csv'))

            for index,csv_file_name in enumerate(tqdm(get_paths(self.file_list, "data/"+self.data_folder), desc="Processing CSV Files",
                                    unit="file")):
                time,pressure = self.GetPressureTime(index,csv_file_name)
                smoothed_pressures = gaussian_filter(pressure,sigma=self.gaussian_filter_sigma)
                self.oringe_pressure_list.append(pressure)
                self.time_list.append(time)
                self.smoothed_pressures_list.append(smoothed_pressures)
                max_index,max_value = self.GetMaxValue(smoothed_pressures)
                max_diff_index,max_diff_value = self.GetMaxDiff(index,smoothed_pressures)
                # 写入csv文件时使用
                self.max_values_list.append([self.file_names[index],max_value])
                self.max_diff_value_list.append([self.file_names[index],max_diff_value])
                self.max_index_list.append(max_index)
                self.max_diff_index_list.append(max_diff_index)
                # 裁剪指定范围压力
                self.slice_smooth_pressure_list.append(smoothed_pressures[self.slice_start_list[index]:])
                self.slice_time_list.append(np.arange(0,len(smoothed_pressures[self.slice_start_list[index]:])) / self.points_one_second_list[index] * 1000)
                self.modify_smooth_pressure_list.append([item - self.modify_pressure_list[index] for item in smoothed_pressures[self.slice_start_list[index]:]])
            self.DrawMainFigure()

    # 获取每个文件的数据
    def GetPressureTime(self, index,csv_file_name):
        file_data = pd.read_csv(csv_file_name, skiprows=self.data["start_row"],header=None)
        voltages = file_data.iloc[:, 1]
        pressures = voltages / 0.725 * voltage_to_pressure_factor(self.deal["unit"])
        times = np.arange(0,len(pressures)) / self.points_one_second_list[index] * 1000
        return times, pressures

    # 绘图流程
    def DrawMainFigure(self):
        fig, ax = plt.subplots(figsize=self.image["size"])
        self.DrawOneData(ax) if self.file_count == 1 else self.DrawMoreData(ax)
        self.DrawCommonData(ax)
        self.OutputImage(file_path=os.path.join(self.image["output_folder"], getOutputFilename(self.title["label"])))
        plt.show() if self.image["is_show"] else ""

    # 保存图片
    def OutputImage(self, file_path):
        plt.savefig(file_path, dpi=self.image["output_dpi"],bbox_inches="tight")

    # 获取最大值和最小值
    def GetMaxValue(self,smoothed_pressures):
        max_index = np.argmax(smoothed_pressures)
        max_value = smoothed_pressures[max_index]
        rounded_max_value = round(max_value, self.deal["rounded"])
        return max_index,max_value

    # 获取最大斜率
    def GetMaxDiff(self,index,smoothed_pressures):
        slice_pressure = smoothed_pressures[int(self.max_pressure_rise_start*self.points_one_second_list[index]):int(self.max_pressure_rise_end*self.points_one_second_list[index])]
        pressure_diffs = np.diff(slice_pressure)
        max_diff_index = np.argmax(pressure_diffs)
        max_diff_value = pressure_diffs[max_diff_index]
        dx = 1/self.points_one_second_list[index]
        return max_diff_index+int(self.max_pressure_rise_start*self.points_one_second_list[index]),max_diff_value/dx/1000
    
    # 将最大爆炸压力及最大升压速率写入csv文件
    def WriteCsvFile(self):
        with open("max_values.csv",'w',newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in self.max_values:
                csv_writer.writerow(row)

        with open("max_diff_values.csv",'w',newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in self.max_diff_values:
                csv_writer.writerow(row)

    # 重置参数
    def ResetParams(self):
        self.mass_list = []
        self.lengend_list = []
        self.time_start_index = []
        self.time_start = []
        self.current = 0
        self.time_list = []
        self.smoothed_pressures_list = []
        self.slice_smooth_pressure_list = []
        self.slice_time_list = []
        self.oringe_pressure_list = []
        self.all_max_index = []
        self.all_max_value = []
        self.all_min_index = []
        self.all_min_value = []
        self.max_values = []
        self.max_diff_values = []
        self.file_count = 0
        self.max_index_list = []
        self.max_diff_index_list = []
        self.max_values_list = []
        self.max_diff_value_list = []
        self.modify_smooth_pressure_list = []
        self.file_names = []
        self.current = 0
    
    # 获取每个文件夹的特有属性
    def GetOneData(self,one_data):
        self.is_gas = one_data["is_gas"]
        self.data_folder = one_data["name"]
        self.points_one_second_list = one_data["points_one_second_list"]
        self.modify_pressure_list = one_data["modify_pressure_list"]
        self.slice_start_list = one_data["slice_start_list"]
        self.xy_lim = one_data["xy_lim"]
        self.title["label"] = one_data["label"]
        self.ncol = one_data["ncol"]
        self.gaussian_filter_sigma = one_data["gaussian_filter_sigma"]
    
    # 绘制一条曲线
    def DrawOneData(self,ax):
        for index, y in enumerate(self.modify_smooth_pressure_list):
            # 绘制压力和压力平滑曲线
            ax.plot(self.time_list[index], self.oringe_pressure_list[index], label=self.mass_list[index])
            ax.plot(self.time_list[index], self.smoothed_pressures_list[index], label=self.mass_list[index]+"(smooth)",linewidth=self.line["linewidth"],color="#ff7e0c")
            # ax.plot(self.slice_time_list[index], self.slice_smooth_pressure_list[index], label=self.mass_list[index]+' $\mathrm{g/m^{3}}$',linewidth=self.line["linewidth"],color="#ff7e0c")
            # 绘制点
            ax.scatter(self.time_list[index][self.max_index_list[index]], self.smoothed_pressures_list[index][self.max_index_list[index]], color='red')
            ax.scatter(self.time_list[index][self.max_diff_index_list[index]], self.smoothed_pressures_list[index][self.max_diff_index_list[index]], color='red')
            # 最大值点
            ax.text(self.time_list[index][self.max_index_list[index]], self.smoothed_pressures_list[index][self.max_index_list[index]], \
                f'最大爆炸压力: ({round(self.time_list[index][self.max_index_list[index]],self.deal["time_rounded"])},\
                    {round(self.max_values_list[index][1],self.deal["rounded"])})', fontsize=self.text["fontsize"], ha=self.text["ha"])
            ax.text(self.time_list[index][self.max_diff_index_list[index]], self.smoothed_pressures_list[index][self.max_diff_index_list[index]], \
                f'最大升压速率: ({round(self.time_list[index][self.max_index_list[index]],self.deal["time_rounded"])},\
                    {round(self.max_diff_value_list[index][1],self.deal["rounded"])})', fontsize=self.text["fontsize"], ha=self.text["ha"])
            ax.legend(bbox_to_anchor=self.lengend["bbox_to_anchor"],prop=self.lengend["prop"],loc=self.lengend["loc"],\
        ncol=self.lengend["ncol"],fancybox=self.lengend["fancybox"],shadow=self.lengend["shadow"])
        
    # 绘制多条曲线
    def DrawMoreData(self,ax):
        for index, y in enumerate(self.modify_smooth_pressure_list):
            ax.plot(self.slice_time_list[index], y, label=self.mass_list[index],linewidth=self.line["linewidth"],color=self.colors[index])
            mass_g = [item if self.is_gas else item + ' $\mathrm{g/m^{3}}$' for item in self.lengend_list]
        ax.legend(bbox_to_anchor=self.lengend["bbox_to_anchor"],prop=self.lengend["prop"],loc=self.lengend["loc"],\
            labels=mass_g,ncol=self.ncol,fancybox=self.lengend["fancybox"],shadow=self.lengend["shadow"],frameon=self.lengend["frameon"])
        
    # 绘图公共参数
    def DrawCommonData(self,ax):
        ax.set_title(label=self.title["label"], pad=self.title["pad"],fontsize=self.font["font_size"]) if self.title["is_show"] else ""
        ax.set_xlabel(self.xy_label["x_label"], labelpad=self.xy_label["labelpad"])
        ax.set_ylabel(self.xy_label["y_label"], labelpad=self.xy_label["labelpad"])
        ax.set_xlim(self.xy_lim["xlim"])
        ax.set_ylim(self.xy_lim["ylim"])
        ax.tick_params(axis='both', direction=self.tick_param['direction'], labelsize=self.tick_param['labelsize'],\
            pad=self.tick_param['pad'],width=self.tick_param['width'],size=self.tick_param['size']) # pad标尺距轴线的距离

        ax.spines['bottom'].set_linewidth(self.spines["linewidth"])  # 设置x轴的轴线粗细
        ax.spines['left'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        ax.spines['top'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        ax.spines['right'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        
        ax.grid(visible=self.grid["visible"],linestyle = self.grid["linestyle"]) if self.grid["visible"] else ax.grid(visible=self.grid["visible"])
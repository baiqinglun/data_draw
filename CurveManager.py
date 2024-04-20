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

# 合成输出文件全名
def get_output_filename(image_name):
    return os.path.basename(image_name).split(".")[0] + ".png"

class CurveManager:
    def __init__(self, file_list=None):
        # 创建默认参数
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
        # 读取配置文件
        with open('settings/curve_settings.json', 'r', encoding='UTF-8') as settings_file:
            settings_data = dict(json.load(settings_file))
            # settings_data = json.load(settings_file)
            self.data_folder = settings_data["data_folder"]
            self.file_names = settings_data["file_names"]
            self.file_list = settings_data["file_names"] if settings_data["file_names"] else os.listdir(
                os.path.join(os.getcwd(), self.data_folder))
            self.file_list.sort(key=lambda x:int(x.split('-')[1]))
            self.data = settings_data["data"]
            self.deal = settings_data["deal"]
            self.max_pressure_rise_start = self.deal["max_pressure_rise_start"]
            self.max_pressure_rise_end = self.deal["max_pressure_rise_end"]
            self.modify_pressure_list = self.deal["modify_pressure_list"]
            self.slice_start_list = self.deal["slice_start_list"]
            self.font = settings_data["font"]
            self.grid = settings_data["grid"]
            self.xy_lim = settings_data["xy_lim"]
            self.line = settings_data["line"]
            self.title = settings_data["title"]
            self.lengend = settings_data["lengend"]
            self.xy_label = settings_data["xy_label"]
            self.tick_param = settings_data["tick_param"]
            self.spines = settings_data["spines"]
            self.image = settings_data["image"]
            self.text = settings_data["text"]
            
            # 中文使用宋体，英文使用新罗马字体
            config = {
                "font.family":'serif',
                "mathtext.fontset":'stix',
                "font.serif": 'timessimsun',
                "font.weight":'bold',
                "font.size":35
            }
            rcParams.update(config)
            plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题
            # 文件信息获取
            if (len(self.file_names) == 0):
                for file in self.file_list:
                    if file.endswith(".CSV"):
                        split_string = file.split("-")
                        self.mass_list.append(split_string[1].split(".")[0])
                        self.lengend_list.append(split_string[1])
                        self.file_names.append(split_string[1]+"-"+split_string[2]+"-"+split_string[3]+"-"+split_string[4])
                        self.file_count += 1
            
            # 如果没有指定各个文件的采集率，全部按照默认值
            if (len(self.data["points_one_second_list"]) == 0):
                self.points_one_second_list = np.full(self.file_count,self.data["default_points_one_second"])
            
            # 如果没有指定各个文件裁剪范围，全部不裁剪
            if len(self.deal["slice_start_list"]) == 0:
                self.slice_start_list = np.full(self.file_count,self.deal["default_slice_start"])
                
            # 如果没有指定各个文件修正值，全部不修正
            if len(self.deal["modify_pressure_list"]) == 0:
                self.modify_pressure_list = np.full(self.file_count,self.deal["default_modify_pressure"])
        
        # 创建输出文件夹
        if self.image["output_folder"] and not os.path.exists(self.image["output_folder"]):
            os.makedirs(self.image["output_folder"])

    # 循环所有csv数据文件，开始处理
    def process_all_csv_files(self):
        for csv_file_name in tqdm(get_paths(self.file_list, self.data_folder), desc="Processing CSV Files",
                                  unit="file"):
            time,pressure = self.get_pressure_time(csv_file_name)
            smoothed_pressures = gaussian_filter(pressure,
                                                 sigma=self.deal["gaussian_filter_sigma"])
            self.oringe_pressure_list.append(pressure)
            self.time_list.append(time)
            self.smoothed_pressures_list.append(smoothed_pressures)
            max_index,max_value = self.getMaxValue(smoothed_pressures)
            max_diff_index,max_diff_value = self.getMaxDiff(self.current,smoothed_pressures)
            # 写入csv文件时使用
            self.max_values_list.append([self.file_names[self.current],max_value])
            self.max_diff_value_list.append([self.file_names[self.current],max_diff_value])
            self.max_index_list.append(max_index)
            self.max_diff_index_list.append(max_diff_index)
            
            # 裁剪指定范围压力
            self.slice_smooth_pressure_list.append(smoothed_pressures[self.slice_start_list[self.current]:])
            self.slice_time_list.append(np.arange(0,len(smoothed_pressures[self.slice_start_list[self.current]:])) / self.points_one_second_list[self.current] * 1000)
            self.modify_smooth_pressure_list.append([item - self.modify_pressure_list[self.current] for item in smoothed_pressures[self.slice_start_list[self.current]:]])
            self.current += 1

    # 获取每个文件的数据
    def get_pressure_time(self, csv_file_name):
        file_data = pd.read_csv(csv_file_name, skiprows=self.data["start_row"],header=None)
        voltages = file_data.iloc[:, 1]
        pressures = voltages / 0.725 * voltage_to_pressure_factor(self.deal["unit"])
        times = np.arange(0,len(pressures)) / self.points_one_second_list[self.current] * 1000
        return times, pressures

    # 绘图
    def draw_main_figure(self):
        fig, ax = plt.subplots(figsize=self.image["size"])
        # 绘制曲线并获得最大值与最大斜率
        if self.file_count == 1:
            for index, y in enumerate(self.modify_smooth_pressure_list):
                # 绘制压力和压力平滑曲线
                ax.plot(self.time_list[index], self.oringe_pressure_list[index], label=self.mass_list[index])
                ax.plot(self.time_list[index], self.smoothed_pressures_list[index], label=self.mass_list[index]+"(smooth)")
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
        else:
            # 绘制多条曲线
            for index, y in enumerate(self.modify_smooth_pressure_list):
                ax.plot(self.slice_time_list[index], y, label=self.mass_list[index],linewidth=self.line["linewidth"])
            mass_g = [item + '$\mathrm{g/m^{3}}$' for item in self.lengend_list]
            ax.legend(bbox_to_anchor=self.lengend["bbox_to_anchor"],prop=self.lengend["prop"],loc=self.lengend["loc"],\
                labels=mass_g,ncol=self.lengend["ncol"],fancybox=self.lengend["fancybox"],shadow=self.lengend["shadow"])
        # 绘图公共参数
        # ax.set_title(label=self.title["label"], pad=self.title["pad"],fontsize=self.font["font_size"])
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
        ax.grid(visible=self.grid["visible"],linestyle = self.grid["linestyle"])
        self.output_image(file_path=os.path.join(self.image["output_folder"], get_output_filename(self.title["label"])))
        if self.image["is_show"]:
            plt.show()

    # 保存图片
    def output_image(self, file_path):
        plt.savefig(file_path, dpi=self.image["output_dpi"],bbox_inches="tight")

    # 获取最大值和最小值
    def getMaxValue(self,smoothed_pressures):
        max_index = np.argmax(smoothed_pressures)
        max_value = smoothed_pressures[max_index]
        rounded_max_value = round(max_value, self.deal["rounded"])
        return max_index,max_value
        
    # 获取最大斜率
    def getMaxDiff(self,index,smoothed_pressures):
        slice_pressure = smoothed_pressures[int(self.max_pressure_rise_start*self.points_one_second_list[index]):int(self.max_pressure_rise_end*self.points_one_second_list[index])]
        pressure_diffs = np.diff(slice_pressure)
        max_diff_index = np.argmax(pressure_diffs)
        max_diff_value = pressure_diffs[max_diff_index]
        dx = 1/self.points_one_second_list[index]
        return max_diff_index+int(self.max_pressure_rise_start*self.points_one_second_list[index]),max_diff_value/dx/1000
    
    # 将最大爆炸压力及最大升压速率写入csv文件
    def writeCsvFile(self):
        with open("max_values.csv",'w',newline='') as csvfile:
             # 创建CSV写入器对象
            csv_writer = csv.writer(csvfile)
            # 循环写入数据列表中的每一行
            for row in self.max_values:
                csv_writer.writerow(row)
            
        with open("max_diff_values.csv",'w',newline='') as csvfile:
             # 创建CSV写入器对象
            csv_writer = csv.writer(csvfile)
            # 循环写入数据列表中的每一行
            for row in self.max_diff_values:
                csv_writer.writerow(row)
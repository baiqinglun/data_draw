import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
from tool import get_output_filename
from matplotlib import rcParams

class BarManager:
    def __init__(self):
        with open('settings/bar_settings.json', 'r', encoding='UTF-8') as settings_file:
            settings_data = json.load(settings_file)
            self.data_file = settings_data["data_file"]
            self.font = settings_data["font"]
            self.image = settings_data["image"]
            self.bar = settings_data["bar"]
            self.xy_label = settings_data["xy_label"]
            self.color = self.bar["color"]
            self.title = settings_data["title"]
            self.bar_width = self.bar["barwidth"]
            self.spines = settings_data["spines"]
            self.xy_lim = settings_data["xy_lim"]
            self.tick_param = settings_data["tick_param"]
            self.grid = settings_data["grid"]
            self.lengend = settings_data["lengend"]
            self.draw = settings_data["draw"]

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
            # plt.rcParams['font.weight'] = 'bold'
        # 创建输出文件夹
        if self.image["output_folder"] and not os.path.exists(self.image["output_folder"]):
            os.makedirs(self.image["output_folder"])

    # 运行
    def run(self):
        self.read_file_data()
        self.draw_figure()
    
    # 获取文件的数据
    def read_file_data(self):
        file_data = pd.read_csv(self.data_file)
        self.mass_list, self.max_origin_pressure_list,self.max_modify_pressure_list, self.max_pressure_rise_list\
            = file_data.iloc[:, 0:4].T.values
        self.mass_list = np.trunc(self.mass_list).astype(int)
        self.max_pressure_list = [self.max_origin_pressure_list[i] - self.max_modify_pressure_list[i] \
            for i in range(len(self.max_origin_pressure_list))]

    # 绘图
    def draw_figure(self):
        fig, ax1 = plt.subplots(figsize=self.image["size"])
        self.x = np.arange(len(self.mass_list))
        ax1.set_xticks(self.x,self.mass_list)
        # 绘制第一个y轴的柱状图
        bars1 = ax1.bar([i - self.bar_width/2 for i in self.x],height=self.max_pressure_list,width=self.bar_width,\
            label=self.xy_label["y1_label"],align='center',color=self.color[0])
        ax1.set_xlabel(self.xy_label["x_label"]+"($\mathrm{g/m^{3}}$)")
        ax1.set_ylabel(f'{self.xy_label["y1_label"]}({self.xy_label["y1_label_unit"]})',\
        # ax1.set_ylabel(self.xy_label["y1_label"]+"($\mathrm{MPa/s}$)",\
            labelpad=self.xy_label["labelpad"]-2,color=self.color[0])
        ax1.tick_params(axis='x', direction='in')
        ax1.tick_params(axis='y', labelcolor=self.color[0], color=self.color[0], direction='in')
        ax1.spines['left'].set_color(self.color[0])
        ax1.spines['right'].set_color(self.color[1])
        x1_tick_labels = ax1.get_xticklabels()
        for x1_label in x1_tick_labels:
            x1_label.set_weight("bold")
        y1_tick_labels = ax1.get_xticklabels()
        for y1_label in y1_tick_labels:
            y1_label.set_weight("bold")
        if self.draw["is_show_text"]:
            for x_pos, height in zip(self.x, self.max_pressure_list):
                ax1.annotate(f'{height:.2f}', (x_pos, height), ha='center', va='bottom', fontsize=20,color=self.color[0])
        
        # 绘制第二个y轴的柱状图
        ax2 = ax1.twinx()
        bars2 = ax2.bar([i + self.bar_width/2 for i in self.x], self.max_pressure_rise_list,self.bar_width,\
            label=self.xy_label["y2_label"],align='center',color=self.color[1])
        ax2.set_ylabel(f'{self.xy_label["y2_label"]}({self.xy_label["y2_label_unit"]})',\
            labelpad=self.xy_label["labelpad"],color=self.color[1])
        ax2.tick_params(axis='y', labelcolor=self.color[1], color=self.color[1], direction='in')
        ax2.spines['left'].set_color(self.color[0])
        ax2.spines['right'].set_color(self.color[1])
        x2_tick_labels = ax2.get_xticklabels()
        for x2_label in x2_tick_labels:
            print(type(x2_label))
            x2_label.set_weight(100)
        y2_tick_labels = ax2.get_yticklabels()
        for y2_label in y2_tick_labels:
            print(y2_label)
            y2_label.set_weight("bold")
        # 调整右侧y轴标题与刻度线的位置
        if self.draw["is_show_text"]:
            for x_pos, height in zip(self.x, self.max_pressure_rise_list):
                    ax2.annotate(f'{height:.2f}', (x_pos + self.bar["barwidth"], height), ha='center', va='bottom',
                                fontsize=20,color=self.color[1])

        # 合并图例，设置字体大小
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        lines = lines1 + lines2
        labels = labels1 + labels2
        legend = plt.legend(lines, labels,bbox_to_anchor=self.lengend["bbox_to_anchor"],\
                prop=self.lengend["prop"],loc=self.lengend["loc"],ncol=self.lengend["ncol"],\
                fancybox=self.lengend["fancybox"],shadow=self.lengend["shadow"])
        # legend.get_frame().set_facecolor('lightgray')  # 设置背景颜色
        # legend.get_frame().set_alpha(0.4)  # 设置透明度
        # ax1.set_xticks(self.x + self.bar["barwidth"] / 2, self.mass_list)

        ax1.set_xlim(self.xy_lim["xlim"])
        ax1.set_ylim(self.xy_lim["y1lim"])
        ax2.set_ylim(self.xy_lim["y2lim"])
        ax1.tick_params(axis='both', direction=self.tick_param['direction'], labelsize=self.tick_param['labelsize'],\
           pad=self.tick_param['pad'],width=self.tick_param['width'],size=self.tick_param['size']) # pad标尺距轴线的距离
        ax2.tick_params(axis='both', direction=self.tick_param['direction'], labelsize=self.tick_param['labelsize'],\
           pad=self.tick_param['pad'],width=self.tick_param['width'],size=self.tick_param['size']) # pad标尺距轴线的距离
        ax1.spines['left'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        ax2.spines['right'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        ax2.spines['bottom'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        ax2.spines['top'].set_linewidth(self.spines["linewidth"])    # 设置y轴的轴线粗细
        
        # 调整右侧空白
        # if self.title["label"] != "":
            # plt.title(self.title["label"],pad=self.title["pad"],fontsize=self.font["font_size"])
        
        self.output_image(file_path=os.path.join(self.image["output_folder"], get_output_filename(self.title["label"])))
        if self.image["is_show"]:
            plt.show()
    def output_image(self, file_path):
        plt.savefig(file_path, dpi=self.image["output_dpi"],bbox_inches="tight")
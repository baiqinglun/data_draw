# 配色

2-5：
`["#f49128","#194a55"]`
![](https://test-123456-md-images.oss-cn-beijing.aliyuncs.com/img/20240425190810.png)

2-6：
`["#ff7710","#020029"]`
![](https://test-123456-md-images.oss-cn-beijing.aliyuncs.com/img/20240425191112.png)

2-7：
`["#e6b900","#194a55"]`
![](https://test-123456-md-images.oss-cn-beijing.aliyuncs.com/img/20240425191258.png)

2-8：
`["#266b69","#ed723e"]`
![](https://test-123456-md-images.oss-cn-beijing.aliyuncs.com/img/20240425191510.png)
# AIBN处理

## 曲线图

```json
{
  "data_folder": "AIBN",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":19256,
    "modify_pressure_list":[41.95,43.85,40.45,39.69,38.68,36.92,33.89],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[50,500],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"AIBN爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图
```json
{
  "data_file": "bar_data/AIBN.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,7],
    "y1lim":[0,900],
    "y2lim":[0,80]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"AIBN最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "AIBN浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# AIBN-APP
## 曲线图
```json
{
  "data_folder": "AIBN-APP",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[19229,59236,135359,59236,59236,59236],
    "default_slice_start":0,
    "modify_pressure_list":[39.67,35.12,31.02,20.65,22.30,16.28],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[80,1000],
    "ylim":[-100,800]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"APP抑制AIBN粉尘爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```
## 柱状图
```json
{
  "data_file": "bar_data/AIBN-APP.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,6],
    "y1lim":[0,800],
    "y2lim":[0,80]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"APP作用下AIBN最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "APP浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# AIBN-DryWater

## 曲线图

```json
{
  "data_folder": "AIBN-DryWater",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[19240,59298,278306,59298,59298,59298],
    "default_slice_start":0,
    "modify_pressure_list":[39.62,34.81,32.02,32.3,25.1,21.4],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[80,800],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"干水抑制AIBN爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/AIBN-DW.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,6],
    "y1lim":[0,1000],
    "y2lim":[0,80]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"干水作用下AIBN最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "干水浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# BPO

## 曲线图

```json
{
  "data_folder": "BPO",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":29276,
    "modify_pressure_list":[42.2,39.9,39.28,41.21,38.22,40,36.43],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[100,500],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"BPO爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/BPO.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,7],
    "y1lim":[0,850],
    "y2lim":[0,70]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"BPO最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "BPO浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# BPO-APP

## 曲线图

```json
{
  "data_folder": "BPO-APP",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":29155,
    "modify_pressure_list":[41.26,35.88,31.04,27.23,20.67,20.35,8.55],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[100,1200],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"APP抑制BPO爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/BPO-APP.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,7],
    "y1lim":[0,800],
    "y2lim":[0,60]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"APP作用下BPO最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "APP浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# BPO-DayWater

## 曲线图

```json
{
  "data_folder": "BPO-DryWater",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[29218,59307,59307,59307,59307],
    "default_slice_start":0,
    "modify_pressure_list":[41.30,28.64,28.07,27.74,4.1],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[80,1300],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"干水抑制BPO爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/BPO-DW.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,5],
    "y1lim":[0,800],
    "y2lim":[0,60]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"干水作用下BPO最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "干水浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# LPO

## 曲线图

```json
{
  "data_folder": "LPO",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[29269,29269,29269,29269,29269,19290,19290],
    "default_slice_start":0,
    "modify_pressure_list":[48.62,46.89,43.63,42.65,40.16,37.44,37.33],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[100,400],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"LPO爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/LPO.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,7],
    "y1lim":[0,800],
    "y2lim":[0,60]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"LPO最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "LPO浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# LPO-APP

## 曲线图

```json
{
  "data_folder": "LPO-APP",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":29292,
    "modify_pressure_list":[42.51,40.37,35.67,27.9,23.82,12.15],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[100,1000],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"APP抑制LPO爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/LPO-APP.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,6],
    "y1lim":[0,800],
    "y2lim":[0,60]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"APP作用下LPO最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "APP浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# LPO-DayWater

## 曲线图

```json
{
  "data_folder": "LPO-DryWater",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 100000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":29358,
    "modify_pressure_list":[42.56,35.53,29.64,15.4,12.10,8.35],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[100,1200],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"干水抑制过氧化双月桂酰粉尘爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":2,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```

## 柱状图

```json
{
  "data_file": "bar_data/LPO-DW.csv",
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[],
    "default_slice_start":0,
    "modify_pressure_list":[],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right",
    "fontweight": "bold"
  },
  "font":{
    "font_size": 40,
    "fontweight":"bold"
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[-1,6],
    "y1lim":[0,800],
    "y2lim":[0,60]
  },
  "bar":{
    "barwidth":0.4,
    "color":["#3535a1","#a54242"]
  },
  "title":{
    "label":"干水作用下LPO最大爆炸压力及最大升压速率",
    "pad":20,
    "fontweight":"bold"
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 28},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "干水浓度",
    "y1_label": "最大爆炸压力",
    "y1_label_unit":"kPa",
    "y2_label": "最大升压速率",
    "y2_label_unit":"MPa/s",
    "labelpad":10,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  },
  "draw":{
    "is_show_text":false
  }
}
```

# 乙炔

## 曲线图

```json
{
  "data_folder": "Acetylene-DryWater",
  "file_names": [],
  "data":{
    "mass":[],
    "start_row": 17,
    "default_points_one_second": 200000,
    "points_one_second_list":[]
  },
  "deal":{
    "gaussian_filter_sigma": 30,
    "unit": "kPa",
    "time_rounded":6,
    "rounded":4,
    "max_diff_start":0.25,
    "max_pressure_rise_start":0.4,
    "max_pressure_rise_end":1.0,
    "slice_start_list":[23457,19424,19424],
    "default_slice_start":0,
    "modify_pressure_list":[37.5,14.3,10.8],
    "default_modify_pressure":0
  },
  "text":{
    "fontsize":10,
    "ha":"right"
  },
  "font":{
    "font_size": 40
  },
  "grid":{
    "visible":true,
    "linestyle":"--"
  },
  "xy_lim":{
    "xlim":[200,500],
    "ylim":[-100,900]
  },
  "line":{
    "linewidth":5
  },
  "title":{
    "label":"干水抑制乙炔爆炸压力曲线",
    "pad":30
  },
  "lengend":{
    "ncol":1,
    "bbox_to_anchor":[1, 1],
    "prop":{"size": 30},
    "loc":"upper right",
    "fancybox":true,
    "shadow":true
  },
  "xy_label":{
    "x_label": "时间(ms)",
    "y_label": "爆炸压力(kPa)",
    "labelpad":15,
    "fontweight":"bold"
  },
  "tick_param":{
    "width":4,
    "size":20,
    "pad":10,
    "labelsize":40,
    "direction":"in"
  },
  "spines":{
    "linewidth":4
  },
  "image":{
    "is_show":true,
    "size":[16,12],
    "output_folder":"image",
    "output_dpi": 300
  }
}
```
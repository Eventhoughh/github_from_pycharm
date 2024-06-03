#
# @Time   : 2023/3/19 
# @Author : wuBerlin
# @File   : 基础折线图.py
from pyecharts.charts import  Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线图对象
line = Line()

line.add_xaxis(["中国","美国","日本"])
line.add_yaxis("GDP", [30 ,20, 10])
# 设置全局配置项set_gobal_opts来设置，
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),   #标题内容和位置
    legend_opts=LegendOpts(is_show=True),  #控制图例是否显示
    toolbox_opts=ToolboxOpts(is_show=True), #控制工具箱是否显示
visualmap_opts=VisualMapOpts(is_show=True), #视觉映射
#  更多pyecharts的内容  可前往官网查询  pyecharts.org
)
# 通过render方法，将代码生成为图像
line.render()

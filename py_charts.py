from pyecharts import options as opts
#导入Pie类
from pyecharts.charts import Pie

#饼图的数据类型，为列表的嵌套：[[key1, value1], [key2, value2]]
x = ['北京','上海','广州','深圳','杭州','成都','武汉','西安','合肥','其他']
y= [288 ,195 ,123 ,213 ,77,61,21,10 ,7 ,55 ]
#使用zip函数后
#再将其中的元组转换成列表
data_pair =  [list(i) for i in zip(x,y)]

def set_pie():
    pie = Pie()
    pie.add(
        series_name = '',
        data_pair = data_pair,
        color = 'red',
        #设置图表的标签(指示图表区域),formatter是设置标签内容格式，在饼图中：{a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
        label_opts = opts.LabelOpts(is_show=True,formatter='{b}:{c} \n ({d}%)'),
        # 是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。
        # radius：扇区圆心角展现数据的百分比，半径展现数据的大小
        # area：所有扇区圆心角相同，仅通过半径展现数据大小
        rosetype = 'radius',
        # 饼图的半径，数组的第一项是内半径，第二项是外半径
        # 默认设置成百分比，相对于容器高宽中较小的一项的一半
        radius=['20%','75%']
    )
    pie.set_global_opts(
        #设置图例形状,位置,orient表示横向还是纵向，horizontal和vertical
        legend_opts=opts.LegendOpts(legend_icon='pin',orient='vertical',pos_right='10%'),
        #设置图表主标题，副标题和标题位置
        title_opts=opts.TitleOpts(title = '各城市互联网职位数量分布'),
    )
    #设置饼图的颜色，可选项，不设也有默认的颜色。
    pie.set_colors(['blue','red','orange','yellow','green','purple','black','brown','pink','grey'])
    return pie

pie = set_pie()
pie.render('饼图1.html')


from pyecharts import options as opts
from pyecharts.charts import Bar
#柱状图的数据格式：x轴和y轴都是列表数据
x = ['java','c++','PHP','Android','iOS','Python','web前端']
y1= [16.33 ,18.97 ,13.06 ,18.79 ,18.83,14.84,14.75]
y2= [27.77 ,33.67 ,22.21 ,32.01 ,32.29,25.97,25.53]

def set_bar():
    #设置初始项，图表高width,宽height，以及网页的名称
    bar = Bar(init_opts=opts.InitOpts(width = '800px',height = '600px',page_title='柱状图'))
    #添加x轴数据
    bar.add_xaxis(xaxis_data = x)
    #添加y轴数据，加上series_name，表示图例
    bar.add_yaxis(series_name = '最低工资',y_axis = y)
    bar.add_yaxis(series_name = '最高工资',y_axis = y)
    #设置全局项
    bar.set_global_opts(
        #设置图表主标题，副标题和标题位置
        title_opts=opts.TitleOpts(title = '各技术职位平均工资'),
        #添加坐标轴名称，位置以及大小，name_gap表示名称与x轴距离，font_size是字体大小
        xaxis_opts = opts.AxisOpts(name = '技术',name_location='center',name_gap=25,name_textstyle_opts=opts.TextStyleOpts(font_size = 15)),
        yaxis_opts = opts.AxisOpts(name = '工资(k/月)')
        )
    return bar

bar = set_bar()
#生成html文件
bar.render('柱状图1.html')

from pyecharts import options as opts
from pyecharts.charts import Line

#折线图的数据格式：x轴和y轴都是列表数据
x = ['java','c++','PHP','Android','iOS','Python','web前端']
y= [22.05 ,26.32 ,17.64 ,25.40 ,25.56,20.41,20.14]


def set_line():
    line = Line()
    line.add_xaxis(xaxis_data = x)
    #添加y轴数据，加上series_name，表示图例
    line.add_yaxis(series_name = '工资',y_axis = y)
    line.set_global_opts(
        #设置图例形状
        legend_opts=opts.LegendOpts(legend_icon='pin'),
        #设置图表主标题，副标题和标题位置
        title_opts=opts.TitleOpts(title = '各技术职位平均工资'),
        #添加坐标轴名称，位置以及大小，name_gap表示名称与x轴距离，font_size是字体大小
        xaxis_opts = opts.AxisOpts(name = '技术类型',name_location='center',name_gap=25,name_textstyle_opts=opts.TextStyleOpts(font_size = 15)),
        yaxis_opts = opts.AxisOpts(name = '工资(k/月)')
        )
    return line

line = set_line()
line.render('折线图1.html')



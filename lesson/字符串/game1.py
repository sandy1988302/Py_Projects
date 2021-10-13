import pygal
from pygal import *  # 导入模块中的所有类
from random import randint

d = 20  # 骰子面数
n = 100  # 掷出骰子次数


class Die:  # 表示一个掷筛子的类
    def __init__(self, num_sides=d):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)  # 调用库randint()方法;返回值：1-6之间的随机数


die = Die()  # 实例化
results = []
for roll_num in range(n):  # 含义：从0-100依次取值，取100次，因此执行100次赋值
    result = die.roll()
    results.append(result)
# print(results)                           #打印每次随机数值

frequencies = []
for value in range(1, die.num_sides + 1):  # 现在值得范围1-6
    frequency = results.count(value)  # 计算列表中value出现的次数
    frequencies.append(frequency)  # 将次数添加到列表中
print(frequencies)  # 打印频次次数

hist = pygal.Bar()  # 对结果可视化
hist.title = "掷骰子" + str(n) + "次每面出现的次数"  # 设置直方图标题
hist.x_labels = []  # x轴标签
for i in range(1, d + 1):
    hist.x_labels.append(str(i))
hist.x_title = "结果"  # x轴标题
hist.y_title = "频次"  # y轴标题
hist.add('D20', frequencies)
hist.render_to_file('die_visual1.svg')  # 生成svg文件

# 计算100次 面频次/总次数
pie = Pie()
pie.title = "掷骰子比例图"  # 百分比图
for i in range(1, d + 1):
    pie.add('D' + str(i), frequencies[i - 1] / 100)
pie.render_to_file('die_visual2.svg')  # 生成svg文件：生成同一个文件(只显示一个)

circle = Pie(inner_radius=0.6)  # 圆环图
circle.title = "掷骰子圆环图"
for i in range(1, d + 1):
    circle.add('D' + str(i), frequencies[i - 1])
circle.render_to_file('die_visual3.svg')

bar = HorizontalBar()  # 水平条形图
bar.title = '掷骰子水平条形图'
for i in range(1, d + 1):
    bar.add('D' + str(i), frequencies[i - 1])
bar.render_to_file('die_visual4.svg')

spot = XY(stroke=False)  # 这部分模拟离散坐标点
spot.title = '掷骰子散点图'
spot_x = [(3, 2), (1, 2), (3, 8), (5, 7), (6, 14)]
spot.add('D20', spot_x)
spot.render_to_file('die_visual5.svg')

line = Line()
line._title = "掷骰子折线图"
line.x_labels = map(str, range(1, d + 1))  # range：7为结束的范围
linelist = []
for i in range(0, d):
    linelist.append(frequencies[i])
line.add('频次数', linelist)
line.render_to_file('die_visual6.svg')

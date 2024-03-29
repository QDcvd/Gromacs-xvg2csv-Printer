# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:53:46 2020

@author: 郝蛤蛤
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import colorsys
import sys
import csv
#定义字体类型
plt.rc('font', family='Times New Roman')

# data = pd.DataFrame(pd.read_csv('RMSD-1.csv', header=1))
# print(data)
filename = sys.argv[1]
unitsx = sys.argv[2]
unitsy = sys.argv[3]
# showfig = sys.argv[4] #0表示不显示, 1表示显示
#读取x轴的数据，也就是第一列数据
datax = pd.read_csv(filename, usecols=[0])
data_x_list = datax.values.tolist()

#区分度高的随机RPG颜色
def get_n_hls_colors(num):
    hls_colors = []
    i = 0
    step = 360.0 / num
    while i < 360:
        h = i
        s = 90 + random.random() * 10
        l = 50 + random.random() * 10
        _hlsc = [h / 360.0, l / 100.0, s / 100.0]
        hls_colors.append(_hlsc)
        i += step

    return hls_colors
    print(hls_colors)

def ncolors(num):
    rgb_colors = []
    if num < 1:
        return rgb_colors
    hls_colors = get_n_hls_colors(num)
    for hlsc in hls_colors:
        _r, _g, _b = colorsys.hls_to_rgb(hlsc[0], hlsc[1], hlsc[2])
        r, g, b = [int(x * 255.0) for x in (_r, _g, _b)]
        rgb_colors.append([r, g, b])
    return rgb_colors

def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)

#读取最后一列第一行的数值，用来作定义域
with open(filename) as csvfile:
    mLines = csvfile.readlines()
    targetLine = mLines[-1]
    lastx = targetLine.split(',')[0]
    lastx = float(lastx)

input_csv = csv.reader(open(filename, 'r'))#读取并判断有多少列数
row_num = ""
for row in input_csv:
    row_num = row
# print(len(row_num))
fig = plt.figure()
colorlist = list(map(lambda x: color(tuple(x)), ncolors(len(row_num))))
#颜色初始化
colorlist.insert(1, 'black')
colorlist.insert(3, 'red')
colorlist.insert(5, 'blue')
colorlist.insert(7, '#046804')
colorlist.insert(9, '#040484')
colorlist.insert(11, '#FF00FF')
print("colorlist:" + str(colorlist))
ranNum_list = []

for num in range(1, len(row_num)):
    # exec('listy' + str(i) + ' = ' + datay.values.tolist())
    while(len(ranNum_list) < len(colorlist)):
        ranNum = random.randint(0, len(colorlist)-1)
        if ranNum not in ranNum_list:
            ranNum_list.append(ranNum)
    print("本次迭代数字" + str(ranNum_list[num - 2]))
    # rancolor = colorlist[ranNum_list[num - 3]]
    rancolor = colorlist[num]
    if num % 2 != 0:
        # print(num)
        datay = pd.read_csv(filename, usecols=[num])
        outfit = str(datay.columns)
        outfit = outfit.replace("Index([\'", "")#正则表达式总是学不会，那我只能暴力替换了
        outfit = outfit.replace("Index([u\'", "")
        outfit = outfit.replace("\'], dtype=\'object\')", "")
        outfit = outfit.replace(".2", "")
        outfit = outfit.replace(".1", "")
        outfit = outfit.replace(".xvg", "")
        #随机颜色
        # colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        # rancolor = ""
        # for i in range(6):
        #     rancolor += colorArr[random.randint(0, 14)]
        # print(rancolor)
        # print(outfit)
        #批量定义
        listy = str(datay.values.tolist())
        exec('listy' + str(num) + ' = ' + listy)  # 批量定义列到变量
        exec('outfit' + str(num) + ' = ' + ' \" ' + outfit + ' \" ')  # 批量定义表头到变量
        # exec('data_y' + str(num) + ' = ' + str('data_y' + str(num)))
        exec('data_y' + str(num) + ' = ' + str("list(" + "listy" + str(num) + ")"))
        exec('DM' + str(num) + '=' + str("fig.add_subplot(1, 1, 1)"))
        exec('DM' + str(num) + '.plot(data_x_list, data_y' + str(num) + ", 'm-', label=outfit"
             + str(num) + ", color='" + rancolor + "'" + ', linewidth=0.5, alpha=0.8)')

DM1.legend(frameon=False)  # 图例，去掉框框
plt.xlim(0, lastx)  # 坐标轴范围
DM1.set_xlabel(unitsx)  # 例如Time(ns)
DM1.set_ylabel(unitsy)  # 例如RMSD(ns)
jpgName = filename.replace('.csv', '.jpg')
plt.savefig(jpgName)



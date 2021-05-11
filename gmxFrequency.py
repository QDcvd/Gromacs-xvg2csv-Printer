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


def frequencyList(bins, data_choiced):  # 此函数用于计算频数并输出频数列表
    # 频数列表
    max_data_choiced = max(data_choiced)
    min_data_choiced = min(data_choiced)
    differentNum = (max_data_choiced - min_data_choiced) / bins

    divideList = []
    for i in range(0, bins):
        area = [min_data_choiced + (differentNum * i), min_data_choiced + (differentNum * (i + 1))]
        divideList.append(area)

    # print(divideList)
    frequencyList = []
    frequencyList_x = []
    for j in range(0, bins):
        frequencyNum = 0
        for single_data in data_choiced:
            if divideList[j][0] < single_data < divideList[j][1]:
                frequencyNum += 1
        frequencyList.append(frequencyNum)
        frequencyList_x.append(divideList[j][0])

    frequencyList = [(x/bins) for x in frequencyList]  # 计算频率
    return frequencyList, frequencyList_x


def reductionList(old_list):  # 降维
    # 把列表转为字符串
    b = str(old_list)
    # 替换掉'['和']'
    b = b.replace('[', '')
    b = b.replace(']', '')
    # 最后转化成列表
    new_list = list(eval(b))
    return new_list


if __name__ == '__main__':
    #定义字体类型
    plt.rc('font', family='Times New Roman')
    #定义分割份数, 默认50
    # bins = 50

    filename = sys.argv[1]
    unitsx = sys.argv[2]
    unitsy = sys.argv[3]
    bins_list = [20, 50, 100, 1000]
    # showfig = sys.argv[4] #0表示不显示, 1表示显示
    # 读取x轴的数据，也就是第一列数据
    datax = pd.read_csv(filename, usecols=[0])
    data_x_list = datax.values.tolist()

    # data_choiced = list(data.iloc[:, 1])
    # # 频数列表
    # max_data_choiced = max(data_choiced)
    # min_data_choiced = min(data_choiced)
    # differentNum = (max_data_choiced - min_data_choiced) / bins
    #
    # divideList = []
    # for i in range(0, bins):
    #     area = [min_data_choiced + (differentNum * i), min_data_choiced + (differentNum * (i + 1))]
    #     divideList.append(area)
    #
    # print(divideList)
    # frequencyList = []
    # for j in range(0, bins):
    #     frequencyNum = 0
    #     for single_data in data_choiced:
    #         if divideList[j][0] < single_data < divideList[j][1]:
    #             frequencyNum += 1
    #     frequencyList.append(frequencyNum)

    # plt.plot(frequencyList(bins, data_choiced))
    # plt.show()

    for bins in bins_list:
        input_csv = csv.reader(open(filename, 'r'))  # 读取并判断有多少列数
        row_num = ""
        for row in input_csv:
            row_num = row
        # print(len(row_num))
        fig = plt.figure()
        colorlist = list(map(lambda x: color(tuple(x)), ncolors(len(row_num))))
        # 颜色初始化
        colorlist.insert(1, 'black')
        colorlist.insert(3, 'red')
        colorlist.insert(5, 'blue')
        colorlist.insert(7, '#046804')
        colorlist.insert(9, '#040484')
        colorlist.insert(11, '#FF00FF')
        print("colorlist:" + str(colorlist))
        ranNum_list = []

        datax_whole = []# 记录所有的csv的x坐标
        datay_whole = []  # 记录所有的csv的y坐标
        for num in range(1, len(row_num)):
            # exec('listy' + str(i) + ' = ' + datay.values.tolist())
            while (len(ranNum_list) < len(colorlist)):
                ranNum = random.randint(0, len(colorlist) - 1)
                if ranNum not in ranNum_list:
                    ranNum_list.append(ranNum)
            print("本次迭代数字" + str(ranNum_list[num - 2]))
            # rancolor = colorlist[ranNum_list[num - 3]]
            rancolor = colorlist[num]
            if num % 2 != 0:
                # print(num)
                # datay = pd.read_csv(filename, usecols=[num])
                data_choiced = pd.read_csv(filename, usecols=[num])
                outfit = str(data_choiced.columns)
                outfit = outfit.replace("Index([\'", "")  # 正则表达式总是学不会，那我只能暴力替换了
                outfit = outfit.replace("Index([u\'", "")
                outfit = outfit.replace("\'], dtype=\'object\')", "")
                outfit = outfit.replace(".2", "")
                outfit = outfit.replace(".1", "")
                outfit = outfit.replace(".xvg", "")
                # 随机颜色
                # colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
                # rancolor = ""
                # for i in range(6):
                #     rancolor += colorArr[random.randint(0, 14)]
                # print(rancolor)
                # print(outfit)
                # 批量定义
                # listy = str(datay.values.tolist())
                data_choiced = reductionList(data_choiced.values.tolist())
                # listy = str(frequencyList(bins, data_choiced))
                list_whole = frequencyList(bins, data_choiced)
                listy = str(list_whole[0])
                listx = list_whole[1]
                # listx = [round(x, 1) for x in listx]  # 四舍五入生成式
                print(listx)
                exec('listx' + str(num) + ' = ' + str(listx))
                exec('listy' + str(num) + ' = ' + listy)  # 批量定义列到变量
                exec('outfit' + str(num) + ' = ' + ' \" ' + outfit + ' \" ')  # 批量定义表头到变量
                # exec('data_y' + str(num) + ' = ' + str('data_y' + str(num)))
                exec('data_y' + str(num) + ' = ' + str("list(" + "listy" + str(num) + ")"))
                exec('data_x' + str(num) + ' = ' + str("list(" + "listx" + str(num) + ")"))
                exec('datax_whole.append(data_x' + str(num) + ')')
                exec('datay_whole.append(data_y' + str(num) + ')')
                exec('DM' + str(num) + '=' + str("fig.add_subplot(1, 1, 1)"))
                exec('DM' + str(num) + '.plot(data_x' + str(num) + ',data_y' + str(num) + ", 'm-', label=outfit"
                     + str(num) + ", color='" + rancolor + "'" + ', linewidth=1, alpha=0.8)')

        datax_whole = reductionList(datax_whole)  # 给大列表降维
        datay_whole = reductionList(datay_whole)  # 给大列表降维
        DM1.legend(frameon=False)  # 图例，去掉框框
        # print(datay_whole)
        plt.xlim(min(datax_whole), round(max(datax_whole), 1))  # 坐标轴范围
        plt.ylim(min(datay_whole), max(datay_whole)*1.1)
        DM1.set_xlabel(unitsx)  # 例如Time(ns)
        DM1.set_ylabel(unitsy + " (%)")  # 例如RMSD(ns)
        # plt.yticks([])

        jpgName = filename.replace('.csv', str(bins))
        jpgName = jpgName + '.jpg'
        plt.savefig(jpgName)




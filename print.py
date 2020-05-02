# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:53:46 2020

@author: 郝蛤蛤
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

func = sys.argv[1]

def print2(filename, x, y1, y2, xlab, ylab):
    data = pd.read_csv(filename)
    data_x = data[x]  # 例如48601-RMSD-potein-potein-xvgx
    data_x_list = data_x.values.tolist()
    # print(data_x_list)
    data1_y = data[y1]  # 例如48601-RMSD-potein-potein-xvgy1
    data1_y_list = data1_y.values.tolist()

    data2_y = data[y2]  # 例如4860-rmsd-potein-potein-xvgy2
    data2_y_list = data2_y.values.tolist()

    fig = plt.figure()

    DM1 = fig.add_subplot(1, 1, 1)
    DM2 = fig.add_subplot(1, 1, 1)

    DM1.plot(data_x_list, data1_y_list, 'm-', label=y1, linewidth=0.5)  # y1轴
    DM2.plot(data_x_list, data2_y_list, 'b-', label=y2, linewidth=0.5)  # y2轴

    DM1.legend(frameon=False)  # 图例，去掉框框

    DM1.set_xlabel(xlab)  # 例如Time(ns)
    DM1.set_ylabel(ylab)  # 例如RMSD(ns)

    plt.show()

def print3(filename, x, y1, y2, y3, xlab, ylab):
    data = pd.read_csv(filename)
    data_x = data[x] #例如48601-RMSD-potein-potein-xvgx
    data_x_list = data_x.values.tolist()
    # print(data_x_list)
    data1_y = data[y1] #例如48601-RMSD-potein-potein-xvgy1
    data1_y_list = data1_y.values.tolist()

    data2_y = data[y2] #例如4860-rmsd-potein-potein-xvgy2
    data2_y_list = data2_y.values.tolist()

    data3_y = data[y3] #例如5018-rmsd-potein-xvgy3
    data3_y_list = data3_y.values.tolist()

    fig = plt.figure()

    DM1 = fig.add_subplot(1, 1, 1)
    DM2 = fig.add_subplot(1, 1, 1)
    DM3 = fig.add_subplot(1, 1, 1)

    DM1.plot(data_x_list, data1_y_list, 'm-', label=y1, linewidth=0.5)  # y1轴
    DM2.plot(data_x_list, data2_y_list, 'b-', label=y2, linewidth=0.5)  # y2轴
    DM3.plot(data_x_list, data3_y_list, 'g-', label=y3, linewidth=0.5)  # y3轴

    DM1.legend(frameon=False)  # 图例，去掉框框

    DM1.set_xlabel(xlab) #例如Time(ns)
    DM1.set_ylabel(ylab) #例如RMSD(ns)

    plt.show()

if func == '3':
    filename = sys.argv[2]
    x = sys.argv[3]
    y1 = sys.argv[4]
    y2 = sys.argv[5]
    y3 = sys.argv[6]
    xlab = sys.argv[7]
    ylab = sys.argv[8]
    print3(filename, x, y1, y2, y3, xlab, ylab)

if func == '2':
    filename = sys.argv[2]
    x = sys.argv[3]
    y1 = sys.argv[4]
    y2 = sys.argv[5]
    xlab = sys.argv[6]
    ylab =sys.argv[7]
    print2(filename, x, y1, y2, xlab, ylab)
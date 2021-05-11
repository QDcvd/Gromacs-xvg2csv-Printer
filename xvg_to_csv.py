# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import os  
import sys, getopt

# 将文件夹中的多个xvg文件汇总到一个csv文件里面
#input_dir = ''
#output_file = ''
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["idir=","ofile="])
    except getopt.GetoptError:
        print(os.path.basename(__file__) + ' -i <inputdir> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(os.path.basename(__file__) + ' -i <inputdir> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', "--idir"):
            input_dir = arg
        elif opt in ('-o', "--ofile"):
            output_file = arg

    # print '输入的文件夹为：' + input_dir
    # print '输出的文件为：' + output_file
    # sys.exit()

    file_dir = input_dir
    # xvg文件所在文件夹
    files = []
    file_df = []
    for _, _, z in os.walk(file_dir):
        files = z
    size = 0
    for filename in files:
        if filename[-1] != 'g':
            continue
        print(filename)
        size = size + 1
        string = []
        index = 0
        for line in open(file_dir + filename):
            if line[0] == '#' or line[0] == '@':
                continue
            temp = line.split(' ')
            buf = []
            for x in temp:
                if x == '':
                    continue
                else:
                    if x[-1] == '\n':
                        x = x[0:len(x) - 1]
                    buf.append(x)
            string.append([])
            for y in buf:
                string[index].append(y)
            index = index + 1
        size_inner = len(string[0])
        name = []
        for i in range(size_inner):
            name.append(filename)
        string.insert(0, name)
        array = np.array(string)
        df = pd.DataFrame(array)
        file_df.append(df)
        
    #print(size)
    # sys.exit()
    if size > 1:
        df = file_df[0]
        for index in range(1, size):
            df = pd.concat([df, file_df[index]], axis = 1, ignore_index=True)       
        df.to_csv(output_file, header = 0, index=0)
    else:
        df = file_df[0]
        df.to_csv(output_file, header = 0, index=0)


if __name__ == "__main__":
    main(sys.argv[1:])

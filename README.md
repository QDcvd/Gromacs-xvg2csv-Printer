# 画普通折线图使用方法 
该脚本用于替代origin繁杂的画图，致力于批量生成折线图

输入： python gmxLineChart.py [文件名称] [x轴名称] [y轴名称]

例子：
python gmxLineChart.py test.csv m m

目前仅支持xvg转换的csv文件。

画图效果:

![dbde635d72787912cc4e5effc7236a9](https://user-images.githubusercontent.com/54057111/117633028-39fa5680-b1b0-11eb-9918-1470d2c46b46.png)
![28c3f121b737edf01dec15536051ea7](https://user-images.githubusercontent.com/54057111/117657540-4096c700-b1cc-11eb-8fd8-2fc99ec58023.jpg)

# 画频率分布折线图使用方法
脚本是基于gmxLineChart.py所做的扩展，以及图表的美化，为了可顺利代替origin的繁杂操作

输入： python gmxFrequency.py [文件名称] [x轴名称] [y轴名称]

例子：
python gmxFrequency.py RMSD-backbone.csv x y

画图效果(一次性输出四种分割形式的频率图)：
分别是20, 50, 100, 1000对数据进行区域划分

![599c62c745b3180003a5204af716c53](https://user-images.githubusercontent.com/54057111/117805418-8a92b200-b28b-11eb-81ca-9e8c17f5700a.jpg)
![8dff81ed061a93f38779c99eb07a681](https://user-images.githubusercontent.com/54057111/117805424-8bc3df00-b28b-11eb-9927-276953d7c7ac.jpg)
![ac8bc1a2a62a62a5dd63da4272093e6](https://user-images.githubusercontent.com/54057111/117805434-8d8da280-b28b-11eb-9e9a-1766a141ae88.jpg)
![38237a013c4b6667ecd5f1ea5df8149](https://user-images.githubusercontent.com/54057111/117805438-8ebecf80-b28b-11eb-9d1b-4784af4f3352.jpg)




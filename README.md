# 画普通折线图使用方法 
输入： python gmxLineChart.py [文件名称] [x轴名称] [y轴名称]

例子：
python gmxLineChart.py test.csv m m

目前仅支持xvg转换的csv文件。

画图效果:

![dbde635d72787912cc4e5effc7236a9](https://user-images.githubusercontent.com/54057111/117633028-39fa5680-b1b0-11eb-9918-1470d2c46b46.png)
![28c3f121b737edf01dec15536051ea7](https://user-images.githubusercontent.com/54057111/117657540-4096c700-b1cc-11eb-8fd8-2fc99ec58023.jpg)

# 画频率分布折线图使用方法
输入： python gmxFrequency.py [文件名称] [x轴名称] [y轴名称]

例子：
python gmxFrequency.py RMSD-backbone.csv x y

画图效果(一次性输出四种分割形式的频率图)：
分别是20, 50, 100, 1000对数据进行区域划分

![671dc0aaf51ef3fe1f05fbeaad0d6ac](https://user-images.githubusercontent.com/54057111/117802321-ec511d00-b287-11eb-9523-47f3a5b4e645.jpg)
![996f51443fc736490ab9b74503b544a](https://user-images.githubusercontent.com/54057111/117802325-ece9b380-b287-11eb-8b95-482bfb3c4291.jpg)
![57b9d5dbffa8b013be6e23f8e330e58](https://user-images.githubusercontent.com/54057111/117802327-ee1ae080-b287-11eb-9af4-32bab7772348.jpg)
![05acfcdef18dd06716d5df0035e083d](https://user-images.githubusercontent.com/54057111/117802332-eeb37700-b287-11eb-84d5-0f85f4c15cf4.jpg)



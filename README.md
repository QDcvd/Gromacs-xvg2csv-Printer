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

![RMSD-backbone50](https://user-images.githubusercontent.com/54057111/117742450-6c02cb80-b237-11eb-8563-fcb67cbe5d68.jpg)
![RMSD-backbone100](https://user-images.githubusercontent.com/54057111/117742452-6dcc8f00-b237-11eb-9eff-b292f3d4954d.jpg)
![RMSD-backbone1000](https://user-images.githubusercontent.com/54057111/117742453-6e652580-b237-11eb-9d74-5f7a356eee5f.jpg)
![RMSD-backbone20](https://user-images.githubusercontent.com/54057111/117742455-6e652580-b237-11eb-9ac9-1a9fc3a9baca.jpg)


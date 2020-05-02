# 使用方法 
当是xyy图时，使用语法：
python print.py 2 [文件名称] [x轴表头名字] [y1轴表头名字] [y2轴表头名字] [x轴标签名字] [y轴标签名字]

当是xyyy图时，使用的语法：
python print.py 3 [文件名称] [x轴表头名字] [y1轴表头名字] [y2轴表头名字] [y3轴表头名字] [x轴标签名字] [y轴标签名字]

例子：
python print.py 3 RMSD.csv 48601-RMSD-potein-potein-xvgx 48601-RMSD-potein-potein-xvgy1 4860-rmsd-potein-potein-xvgy2 5018-rmsd-potein-xvgy3 Time(ns) RMSD(ns)

python print.py 2 RMSD.csv 48601-RMSD-potein-potein-xvgx 48601-RMSD-potein-potein-xvgy1 4860-rmsd-potein-potein-xvgy2 Time(ns) RMSD(ns)

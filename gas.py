# -*- coding:utf-8 -*-
import easygui
easygui.msgbox("距离下一个加油站还有200KM")
size = float(easygui.integerbox("你的油箱有多大",
                                upperbound=9999))
full = float(easygui.integerbox("你油箱有多满(按百分比),",
                                upperbound=100))
km = float(easygui.integerbox("你汽车每升可以走多少千米",
                              upperbound=9999))
all = (size * (full/100)) * km
if all >= 200:
    easygui.msgbox("油箱大小:" + str(size) + "L\n油箱还有多少(百分比):" + str(full) + "%\n每升可以走:" + str(km) + "km\n你还可以走:" + str(
        all) + "km\n你可以去下一个加油站加油")
else:
    easygui.msgbox("油箱大小:" + str(size) + "L\n油箱还有多少(百分比):" + str(full) + "%\n每升可以走:" + str(km) + "km\n你还可以走:" + str(
        all) + "km\n你需要在本站加油")
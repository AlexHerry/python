# -*-coding:utf-8 -*-
import easygui
easygui.msgbox("我们现在促销活动，花费金额10元以下或等于10元，那么有10%的折扣。如果大于10元，那么有20%的折扣")
cost = float(easygui.integerbox("你要花费多少元呢",
                                upperbound=999999))
if cost <= 10:
    a = cost * 0.9
    easygui.msgbox("那么你将会花费"+str(a)+"元")
else:
    b = cost * 0.8
    easygui.msgbox("那么你将会花费"+str(b)+"元")
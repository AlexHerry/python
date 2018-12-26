# -*-coding:utf-8 -*-
import easygui
easygui.msgbox("这个程序将华氏度改为摄氏度")
F = float(easygui.integerbox("请输入一个华氏度温度:",
                       lowerbound=-999,
                       upperbound=999))
C = 5.0 / 9 * (F-32)
easygui.msgbox("它的摄氏度温度是:"+ str(C))
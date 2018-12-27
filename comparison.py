# -*-coding:utf-8 -*-
import easygui
num = float(easygui.enterbox("请输入一个数字"))
if num > 30 and num <= 40:
    easygui.msgbox("这个数字介于30和40之间")
else:
    easygui.msgbox("这个数字不在30和40之间")
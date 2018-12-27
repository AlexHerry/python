#-*-coding:utf-8 -*-
import easygui
easygui.msgbox("我们正在寻找10-12岁的女孩")
while(1):
    sex = easygui.enterbox("你是男孩还是女孩。如果你是男生，请输入m;如果你是女生，请输入f")
    if sex == 'm' or sex == 'f':
        break;
    else:
        easygui.msgbox("请输入正确的性别")
if sex == 'm':
    easygui.msgbox("你不可以加入我们的球队")
else:
    age = easygui.integerbox("你现在几岁了")
    if age >= 10 and age <= 12:
        easygui.msgbox("你可以加入我们的球队")
# -*- coding:utf-8 -*-
import easygui
passwd = "123456"
guess = easygui.enterbox("请输入密码")
if guess == passwd:
    easygui.msgbox("密码正确，欢迎使用")
else:
    easygui.msgbox("密码错误")
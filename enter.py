# -*- coding:utf-8 -*-
import easygui
test = float(easygui.enterbox("你最喜欢吃那种口味的冰淇淋?"))
easygui.msgbox("you choose" + str(test))
# -*- coding:utf-8 -*-
import easygui
test = easygui.buttonbox("你最喜欢吃那种口味的冰淇淋?",
                         choices = ['草莓','芒果','香草'])
easygui.msgbox("你选择" + test)
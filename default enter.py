# -*- coding:utf-8 -*-
import easygui
test = easygui.enterbox("你最喜欢吃那种口味的冰淇淋?",
                        default="香草")
easygui.msgbox("you choose" + test)
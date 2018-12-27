# -*- coding:utf-8 -*-
import easygui
name = easygui.enterbox("你叫什么")
room = easygui.enterbox("你的房间号，街道和城市是什么")
province = easygui.enterbox("你在那个省")
postal = easygui.integerbox("你的邮编是多少",
                            lowerbound=0,
                            upperbound=999999999999)
easygui.msgbox(str(name)+"\n"+str(room)+"\n"+str(province)+"\n"+str(postal))
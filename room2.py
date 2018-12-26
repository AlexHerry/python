# -*- coding:gb2312 -*-
print "询问房间大小，并计算需要多少毛毯"
L = float(input("房间长多少（m）?\n"))
W = float(input("房间宽多少（m）?\n"))
S = L * W
room_Sq = S * 9
carpet = float(input("请输入一块地毯的大小（平方米）:\n"))  #一块地毯的大小，单位平方米
money = input("一块地毯多少钱?\n")
carpet_Sq = carpet * 9
cost = S / carpet  #需要多少块
all = cost * money
print "假设每块地毯",carpet,"平米，也就是",carpet_Sq,"平方尺，那么需要",cost,"块，那么房间的大小是",S,"平米，也就是",room_Sq,"平方尺,需要",all,"元"

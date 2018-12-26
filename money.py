# -*- coding:gb2312 -*-
print "计算零钱的总面额"
five = int(input("有多少个五分币?\n"))
two = int(input("有多少个二分币?\n"))
one = int(input("有多少个一分币?\n"))
five_cost = five * 5
two_cost = two * 2
one_cost = one * 1
all = five_cost + two_cost + one_cost
print "一共",all,"分币"

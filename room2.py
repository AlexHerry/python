# -*- coding:gb2312 -*-
print "ѯ�ʷ����С����������Ҫ����ë̺"
L = float(input("���䳤���٣�m��?\n"))
W = float(input("�������٣�m��?\n"))
S = L * W
room_Sq = S * 9
carpet = float(input("������һ���̺�Ĵ�С��ƽ���ף�:\n"))  #һ���̺�Ĵ�С����λƽ����
money = input("һ���̺����Ǯ?\n")
carpet_Sq = carpet * 9
cost = S / carpet  #��Ҫ���ٿ�
all = cost * money
print "����ÿ���̺",carpet,"ƽ�ף�Ҳ����",carpet_Sq,"ƽ���ߣ���ô��Ҫ",cost,"�飬��ô����Ĵ�С��",S,"ƽ�ף�Ҳ����",room_Sq,"ƽ����,��Ҫ",all,"Ԫ"

# -*-coding:utf-8 -*-
import random
import easygui
secret = random.randint(1,250)
guess = 0
tries = 0
easygui.msgbox("我有一个秘密,它是1到250之间的数字，我会给你12次尝试。")
while guess != secret and tries < 12:
    guess = easygui.integerbox("你的猜测是什么？\n",
                                default=0,
                               lowerbound=0,
                               upperbound=250)
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + "太小了，再大点。")
    elif guess > secret:
        easygui.msgbox(str(guess) + "太大了，再小点。")
    tries += 1

if guess == secret:
    easygui.msgbox("你猜对了")
else:
    easygui.msgbox("朋友，不能再猜了，祝你下次好运,这个数字是" + str(secret))
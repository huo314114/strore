'''
import random
randint_num=random.randint(0,10)
while True:
    num=int(input("请输入一个数字"))
    if num ==randint_num:
        print("ok,")
        break
    elif num>randint_num:
        print("你输入的过大")
    elif num<randint_num:
        print("你输入的过小")
'''

import random
a=random.randint(0,100)
money=1000
i=1
num = int(input("请输入一个数字"))
while money>0:
    if a==num:
        print("ok")
        money = money -100
        print('金额:', money)
        break
    else:
        print("猜错了,再试试")
        print('猜的次数',i)
        money = money - 100
        print('金额:',money)
        num = int(input("请输入一个数字"))
    i = i + 1
print("游戏结束")

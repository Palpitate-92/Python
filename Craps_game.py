# -*- coding: utf-8 -*-
# Craps_game.py
# @author Suyi
# @email suyi067113@gmail.com
# @description Craps赌博游戏，默认为玩家破产或者玩家赚到5w游戏结束
# @created 2021-06-19T23:17:46.224Z+08:00
# @last-modified 2021-06-19T23:24:04.772Z+08:00
#

from random import randint

money = int(input('请输入你的资产(一般情况下你现在手上的钱少于1w): '))
while money > 0 and money < 50000:
    print('你的总资产为:%d' % money)
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        money += debt
        print('玩家胜!')
        continue
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('庄家胜!')
        continue
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == first:
            money += debt
            print('玩家胜!')
        elif current == 7:
            money -= debt
            print('庄家胜!')
        else:
            needs_go_on = True
if money < 0:
    print('你破产了，游戏结束!')
else:
    print('你赚了大钱，即将成为人生赢家!')
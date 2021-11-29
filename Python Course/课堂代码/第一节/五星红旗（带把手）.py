from turtle import *
# 旗帜
width(4)
color('red', 'red')
begin_fill()
pencolor('red')
pu()
goto(0, -300)
pd()
lt(90)
forward(500)
right(90)
forward(300)
right(90)
forward(180)
right(90)
forward(300)
right(90)
end_fill()


# 五角星
# x,y 起始位置； z 大小； a 角度
def drawStar(x, y, z, a=0):
    pencolor('yellow')
    pu()
    goto(x, y)
    pd()
    seth(a)
    for i in range(5):
        fd(z)
        rt(144)


color('yellow', 'yellow')
begin_fill()
drawStar(25, 160, 50)  #2
end_fill()
begin_fill()
# drawStar(110, 170, 20) #3
drawStar(95, 180, 20, 340)  #3
end_fill()
begin_fill()
drawStar(130, 160, 20, 250)  #4
end_fill()
begin_fill()
drawStar(110, 125, 20)  #5
end_fill()
begin_fill()
drawStar(85, 110, 20, 345)  #6
end_fill()
pu()
goto(1000, 1000)
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口
done()
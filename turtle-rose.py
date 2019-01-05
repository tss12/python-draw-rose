import turtle

import time

turtle.speed(5) #画笔移动的速度

  

# 设置初始位置  

turtle.penup()  #提起画笔，移动画笔但并不会绘制图形

turtle.left(90)  #逆时针转动画笔90度

turtle.fd(200)  

turtle.pendown()  #放下画笔，移动画笔即开始绘制

turtle.right(90)  

#设置画笔的大小
turtle.pensize(2)


# 花蕊  

turtle.fillcolor("red")  #填充颜色

turtle.begin_fill()  #开始填充

turtle.circle(10,180)  

turtle.circle(25,110)  

turtle.left(50)  

turtle.circle(60,45)  

turtle.circle(20,170)  

turtle.right(24)  

turtle.fd(30)  

turtle.left(10)  

turtle.circle(30,110)  

turtle.fd(20)  

turtle.left(40)  

turtle.circle(90,70)  

turtle.circle(30,150)  

turtle.right(30)  

turtle.fd(15)  

turtle.circle(80,90)  

turtle.left(15)  

turtle.fd(45)  

turtle.right(165)  

turtle.fd(20)  

turtle.left(155)  

turtle.circle(150,80)  

turtle.left(50)  

turtle.circle(150,90)  

turtle.end_fill()  #结束填充

   

# 花瓣1  

turtle.left(150)  

turtle.circle(-90,70)  

turtle.left(20)  

turtle.circle(75,105)  

turtle.setheading(60)  

turtle.circle(80,98)  

turtle.circle(-90,40)  

  

# 花瓣2  

turtle.left(180)  

turtle.circle(90,40)  

turtle.circle(-80,98)  

turtle.setheading(-83)  

  

# 叶子1  

turtle.fd(30)  

turtle.left(90)  

turtle.fd(25)  

turtle.left(45)  

turtle.fillcolor("green")  

turtle.begin_fill()  

turtle.circle(-80,90)  

turtle.right(90)  

turtle.circle(-80,90)  

turtle.end_fill()  

   

turtle.right(135)  

turtle.fd(60)  

turtle.left(180)  

turtle.fd(85)  

turtle.left(90)  

turtle.fd(80)  

   

# 叶子2  

turtle.right(90)  

turtle.right(45)  

turtle.fillcolor("green")  

turtle.begin_fill()  

turtle.circle(80,90)  

turtle.left(90)  

turtle.circle(80,90)  

turtle.end_fill()  

   

turtle.left(135)  

turtle.fd(60)  

turtle.left(180)  

turtle.fd(60)  

turtle.right(90)  

turtle.circle(200,50)  #画一个圆 200 是半径，50 是弧度

#不让自动退出,放在程序的最后一行
#不然画画结束后会自动退出
turtle.done()

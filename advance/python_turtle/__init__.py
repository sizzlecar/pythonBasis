import turtle


def print_turtle_pos(tur):
    print(tur.position())


"""
turtle.pensize(2)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.mainloop()
"""

"""turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()
"""

# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
turtle.shape("turtle")
print_turtle_pos(turtle)
# 抬笔
turtle.penup()
# 移动至50,50
turtle.goto((50, 50), None)
# 落笔
turtle.pendown()

turtle.dot(20, "red")

# 绘制一个长为100的正方形
for x in range(4):
    turtle.forward(100)
    turtle.left(90)

# 绘制左眼
turtle.penup()
turtle.goto((75, 125), None)
turtle.pendown()
turtle.circle(5, 360)

# 绘制右眼
turtle.penup()
turtle.goto((125, 125), None)
turtle.pendown()
turtle.circle(5, 360)

# 绘制鼻子
turtle.penup()
turtle.goto((95, 70), None)
turtle.pendown()
turtle.forward(10)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(30)
turtle.left(90)

# 绘制嘴巴
turtle.penup()
turtle.goto((80, 60), None)
turtle.pendown()
turtle.forward(50)

turtle.stamp()


turtle.mainloop()

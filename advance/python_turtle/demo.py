import turtle


# turtle.hideturtle()

def go(x, y):
    turtle.goto(20, 50)


turtle.shape("turtle")
turtle.color("red", "yellow")
turtle.begin_fill()
for x in range(4):
    turtle.fd(100)
    turtle.left(90)
turtle.end_fill()

turtle.onclick(go)

# turtle.clearstamp(stamp_id)

'''mick = turtle.Turtle()
joe = mick.clone()

joe.goto((80, 100))
'''
turtle.mainloop()

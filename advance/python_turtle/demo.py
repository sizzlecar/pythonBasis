import turtle

# turtle.hideturtle()

turtle.shape("turtle")
turtle.color("red", "yellow")
turtle.begin_fill()
for x in range(4):
    turtle.fd(100)
    turtle.left(90)
turtle.end_fill()
# turtle.clearstamp(stamp_id)

'''mick = turtle.Turtle()
joe = mick.clone()

joe.goto((80, 100))
'''
turtle.mainloop()

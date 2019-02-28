import turtle

turtle.pensize(3)


turtle.begin_poly()
for y in range(5):
    turtle.forward(100)
    turtle.left(144)

turtle.end_poly()

p = turtle.get_poly()


turtle.register_shape("xx", p)
turtle.shape("xx")

turtle.mainloop()

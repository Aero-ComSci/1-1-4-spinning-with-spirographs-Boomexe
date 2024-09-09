import turtle as t

window = t.Screen()
turtle = t.Turtle()
square_width = 10
increment = 10
colors = ["red", "blue", 'green', 'orange', 'pink', 'black']

turtle.speed(0)

def draw_square():
    global square_width
    turtle.color(colors[square_width // 5 % 5])
    turtle.pendown()
    for i in range(4):
        turtle.forward(square_width * 2)
        turtle.right(90)
    turtle.penup()
    square_width += increment
    turtle.left(90)
    turtle.forward(increment)
    turtle.left(90)
    turtle.forward(increment)
    turtle.right(180)

for i in range(10):
    draw_square()

window.setup(width=0.5, height=0.5)

window.mainloop()

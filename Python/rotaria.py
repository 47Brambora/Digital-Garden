import turtle as t

t.bgcolor("black")
t.hideturtle()
t.speed(0)

for _ in range(36):
    t.color("#BFA3D8")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.right(10)

for _ in range(36):
    t.color("#946EB6")
    t.circle(100)
    t.right(10)

t.penup()
t.begin_fill()
t.forward(50)
t.right(-90)
t.pendown()

t.begin_fill()
t.color("#E5BC64")
t.circle(50)
t.end_fill()
t.color("#BF9D55")
t.circle(50)

t.done()

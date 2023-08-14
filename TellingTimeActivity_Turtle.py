import turtle
import time
import math

window = turtle.Screen()
window.bgcolor("white")
window.setup(width=400, height=400)
window.title("Telling Time v.Turtle")
window.tracer(0)

# Drawing Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(pen):
    # Draw clock
    pen.up()
    pen.goto(0, -150)
    pen.setheading(0)
    pen.color("black")
    pen.pendown()
    pen.circle(150)

    # Draw Hour + Numbers
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for hour in range(1, 13):
        pen.fd(135)
        pen.pendown()
        pen.fd(15)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

        # Draw the numbers at hour positions
        x_pos = 120 * math.cos(math.radians(90 - 30 * hour))
        # Adjust the y-position
        y_pos = 110 * math.sin(math.radians(90 - 30 * hour))
        pen.goto(x_pos, y_pos)
        pen.write(str(hour), align="center", font=("Courier", 14, "bold"))
        pen.goto(0, 0)
        pen.rt(30)

    # Draw Minute
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(60):
        pen.fd(140)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(6)

    # Draw Hands
    hands = [("green", 60, 12), ("blue", 110, 60), ("red", 100, 60)]
    current_time = time.localtime()
    time_set = (current_time.tm_hour, current_time.tm_min, current_time.tm_sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part / hand[2]) * 360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])


def update_clock():
    pen.clear()
    draw_clock(pen)
    window.update()
    # Update the clock every 1000 milliseconds (1 second)
    window.ontimer(update_clock, 1000)


update_clock()
window.mainloop()

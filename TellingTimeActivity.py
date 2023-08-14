###### TELLING TIME ACTIVITY!!!
###By Dom

import tkinter as tk
import math

Width = 400
Height = 400

root = tk.Tk()
root.title("Telling Time")

canvas = tk.Canvas(root, width=Width, height=Height, bg="white")
canvas.pack()

def draw_hand(angle, length, width, color):
    x = Width / 2 + length * Width / 2 * math.cos(angle)
    y = Height / 2 + length * Height / 2 * math.sin(angle)
    canvas.create_line(Width / 2, Height / 2, x, y, fill=color, width=width)

def updateClock():
    canvas.delete("all")
    hour = 9
    minute = 15
    second = 0

    # Draw Clock Face
    canvas.create_oval(2, 2, Width, Height, outline="black", width=3)

    # Draw Numbers
    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = Width / 2 + 0.78 * Width / 2 * math.cos(angle)
        y = Height / 2 + 0.78 * Height / 2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y - 10, text=str(i + 12), font=("Courier", 16))
        else:
            canvas.create_text(x, y, text=str(i), font=("Courier", 16))

    # Draw Lines
    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = Width / 2 + 0.87 * Width / 2 * math.cos(angle)
        y1 = Height / 2 + 0.87 * Height / 2 * math.sin(angle)
        x2 = Width / 2 + 0.98 * Width / 2 * math.cos(angle)
        y2 = Height / 2 + 0.98 * Height / 2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

    # Draw clock hands
    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    second_angle = second * math.pi / 30 - math.pi / 2

    draw_hand(hour_angle, 0.3, 6, "green")
    draw_hand(minute_angle, 0.69, 4, "blue")
    draw_hand(second_angle, 0.65, 2, "red")

    root.after(1000, updateClock)

updateClock()

root.mainloop()

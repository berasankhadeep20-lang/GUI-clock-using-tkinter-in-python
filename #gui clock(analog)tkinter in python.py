#gui clock(analog)tkinter in python
from tkinter import *
import time
import math
root = Tk()
root.title("Analog Clock")
canvas = Canvas(root, width=400, height=400, bg='white')
canvas.pack()
def update_clock():
    canvas.delete("all")
    canvas.create_oval(50, 50, 350, 350, outline='black', width=2)
    for i in range(12):
        angle = math.radians(i * 30)
        x = 200 + 140 * math.sin(angle)
        y = 200 - 140 * math.cos(angle)
        canvas.create_text(x, y, text=str(i if i != 0 else 12), font=('Arial', 14))
    t = time.localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec
    hour_angle = math.radians((hours + minutes / 60) * 30)
    minute_angle = math.radians((minutes + seconds / 60) * 6)
    second_angle = math.radians(seconds * 6)
    hour_x = 200 + 80 * math.sin(hour_angle)
    hour_y = 200 - 80 * math.cos(hour_angle)
    minute_x = 200 + 120 * math.sin(minute_angle)
    minute_y = 200 - 120 * math.cos(minute_angle)
    second_x = 200 + 140 * math.sin(second_angle)
    second_y = 200 - 140 * math.cos(second_angle)
    canvas.create_line(200, 200, hour_x, hour_y, fill='black', width=4)
    canvas.create_line(200, 200, minute_x, minute_y, fill='blue', width=2)
    canvas.create_line(200, 200, second_x, second_y, fill='red', width=1)
    root.after(1000, update_clock)
update_clock()
root.mainloop()
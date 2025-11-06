#gui clock(digital)tkinter in python
from tkinter import *
import time
root = Tk()
root.title("Digital Clock")
def clock():
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
    am_pm = time.strftime("%p")
    time_string = h + ":" + m + ":" + s + " " + am_pm
    label.config(text=time_string)
    label.after(1000, clock)
label = Label(root, font=("Arial", 50), bg="black", fg="white")
label.pack(anchor='center')
clock()
root.mainloop()

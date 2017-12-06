from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def steps(x):
    for i in range(20):
        box = 15
        box += i * 10
        canvas.create_rectangle(box - x, box - x, box + x, box + x, fill = "purple")

steps(5)

root.mainloop()
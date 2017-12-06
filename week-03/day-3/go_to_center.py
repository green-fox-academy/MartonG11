from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
a = 0
b = 150
c = 150
d = 0
e = 150
f = 300

def create_line(x, y):
    canvas.create_line(x, y, 150, 150, fill="red", width="3")

create_line(a, b)
create_line(c, d)
create_line(e, f)

root.mainloop()
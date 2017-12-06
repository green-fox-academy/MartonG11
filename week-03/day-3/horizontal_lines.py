from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

a = 0
b = 10
c = 0
d = 100
e = 0
f = 200

def create_line(x, y):
    canvas.create_line(x, y, (x+50), y, fill="green", width="3") 

create_line(a, b)
create_line(c, d)
create_line(e, f)

root.mainloop()
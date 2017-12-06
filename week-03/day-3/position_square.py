from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

a = 0
b = 0
c = 100
d = 100
e = 200
f = 200

def create_square(x, y):
    canvas.create_rectangle(x, y, (x+50), (y+50), fill="green")

create_square(a, b)
create_square(c, d)
create_square(e, f)

root.mainloop()
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

size1 = 130
size2 = 100
size3 = 50

def draw_square(square_size):
    canvas.create_rectangle(150-(square_size), 150-(square_size),150+(square_size), 150+(square_size), fill="green")

draw_square(size1)
draw_square(size2)
draw_square(size3)

root.mainloop()
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

size1 = 145
color1 = "red"
size2 = 120
color2 = "yellow"
size3 = 100
color3 = "green"
size4 = 80
color4 = "blue"
size5 = 60
color5 = "purple"

def square_draw(x_size, x_color):
    canvas.create_rectangle(150-(x_size), 150-(x_size),150+(x_size), 150+(x_size), fill=x_color)

square_draw(size1, color1)
square_draw(size2, color2)
square_draw(size3, color3)
square_draw(size4, color4)
square_draw(size5, color5)

root.mainloop()
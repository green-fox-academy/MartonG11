from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

BlueBox = canvas.create_rectangle(25, 25, 50, 50, fill="blue")
GreenBox = canvas.create_rectangle(55, 55, 100, 100, fill="green")
RedBox = canvas.create_rectangle(105, 105, 205, 205, fill="red")
YellowBox = canvas.create_rectangle(0, 150, 150, 300, fill="yellow")

root.mainloop()
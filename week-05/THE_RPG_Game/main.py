from tkinter import *
from map_draw import Tiles

root = Tk()
root.title('DAMN RPG SO MUCH FUN')
canvas = Canvas(root, width = 720, height = 720, bg="white", bd=0)

map_draw = Tiles()

class Tile():

    def __init__(self):
        self.floor = PhotoImage(file = 'assets/floor.png')
        self.wall = PhotoImage(file = 'assets/wall.png')
        self.drawer(map_draw.tiles)

    def drawer(self, map):
        for y in range(len(map_draw.tiles)):
            for x in range(len(map_draw.tiles)):
                if map_draw.tiles[y][x] == 0:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.floor)
                else:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.wall)

class Hero(object):
    def __init__(self):
        self.Hero_down = PhotoImage(file = 'assets/hero-down.png')
        self.draw_hero()

    def draw_hero(self):
        self.hero_img = canvas.create_image(0, 0, anchor = NW, image = self.Hero_down)




canvas.pack()
map_drawer = Tile()
hero = Hero()

canvas.focus_set()
root.mainloop()
from tkinter import *
from map_draw import Tiles

root = Tk()
root.title('DAMN RPG SO MUCH FUN')
canvas = Canvas(root, width = 720, height = 720, bg="white", bd=0)

playmap = Tiles()

class Tile():

    def __init__(self):
        self.floor = PhotoImage(file = 'assets/floor.png')
        self.wall = PhotoImage(file = 'assets/wall.png')
        self.drawer(playmap.tiles)

    def drawer(self,the_map):
        for y in range(len(playmap.tiles)):
            for x in range(len(playmap.tiles)):
                if playmap.tiles[y][x] == 0:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.floor)
                else:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.wall)

class Hero(object):
    
    def __init__(self):
        self.Hero_down = PhotoImage(file = 'assets/hero-down.png')
        self.Hero_up = PhotoImage(file = 'assets/hero-up.png')
        self.Hero_left = PhotoImage(file = 'assets/hero-left.png')
        self.Hero_right = PhotoImage(file = 'assets/hero-right.png')
        self.draw_hero()

    def move(self, dx, dy):
        canvas.move(hero.hero_img, dx, dy)

    def draw_hero(self):
        self.hero_img = canvas.create_image(0, 0, anchor = NW, image = self.Hero_down)
    
    def moving_motion(self,motion):
        self.motion = motion
        canvas.itemconfigure(self.hero_img, image = self.motion)




    def arrow_move(self, e):
        if e.keysym == 'Down':
            self.move(0, 72)
            self.moving_motion(self.Hero_down)
        elif e.keysym == 'Up':
            self.move(0, -72)
            self.moving_motion(self.Hero_up)
        elif e.keysym == 'Left':
            self.move(-72, 0)
            self.moving_motion(self.Hero_left)
        elif e.keysym == 'Right':
            self.move(72, 0)
            self.moving_motion(self.Hero_right)



canvas.pack()

map_drawer = Tile()
hero = Hero()
root.bind("<KeyPress>", hero.arrow_move)
canvas.focus_set()
root.mainloop()
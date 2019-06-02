# !/usr/bin/python3
from tkinter import *
#noob u forget comments to add and commit log
from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

coord = 10, 10, 240, 210
arc = C.create_arc(coord, start = -90, extent = 350, fill = "red")
C.pack()
top.mainloop()
#my comment at the end

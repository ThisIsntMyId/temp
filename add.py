from tkinter import *
from tkinter import ttk

def get_sum(event):
    sum = int(no1.get()) + int(no2.get())
    res.delete(0, "end")
    res.insert(0, sum)

root = Tk()

no1 = Entry(root)
no1.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

no2 = Entry(root)
no2.pack(side=LEFT)

equals = Button(root, text="=")
equals.bind("<Button-1>", get_sum)
equals.pack(side=LEFT)

res = Entry(root)
res.pack(side=LEFT)

root.mainloop()

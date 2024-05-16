from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=500)
canvas.pack()
my_image = PhotoImage(file='/home/runner/pythonTkPINE/test.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)

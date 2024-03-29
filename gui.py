import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("1920x1080")

on_btn = PhotoImage(file='on1.png')
off_btn = PhotoImage(file='off1.png')
sensor_btn = PhotoImage(file='sensor.png')
Button(root, image=on_btn).pack(pady=10)


Button(root, image=off_btn).pack(pady = 10)


Button(root, image=sensor_btn, bd = '5').pack(pady = 10)

root.mainloop()

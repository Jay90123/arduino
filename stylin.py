from tkinter import *

root = Tk()
root.title('this should work')
root.geometry("400x400")


def thing():
    my_label.config(text="you clicked the button...")


login_btn = PhotoImage(file='off.png')
img_label = Label(image=login_btn)

mybutton = Button(root, image=login_btn, command=thing)
mybutton.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

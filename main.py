from tkinter import *
from tkinter.ttk import *

from time import strftime

# create the ui
root = Tk()
root.title("Clock")


# function to get the time
def time():
    str_time = strftime("%H:%M:%S %p")
    label.config(text=str_time)
    label.after(1000, time)


# creating a label and packing it
label = Label(root, font=("digifont", 80), background="black", foreground="cyan")
label.pack(anchor='center')

# calling function to display clock
time()
mainloop()

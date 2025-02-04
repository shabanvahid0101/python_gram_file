import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.config()
#set size window
root.geometry('800x600')
#set left and right from monitor
root.geometry('+50+50')
##set max size for windows
root.maxsize(800,600)
##set min size for windows
root.minsize(700,500)
#set title
root.title()
#view app
root.mainloop()
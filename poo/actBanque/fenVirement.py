import tkinter as tk
import compte as c
import banque as b
import json as j


def open(ba:b.Banque, co:c.Compte):

    root = tk.Tk()
    root.title('Tkinter Window Demo')
    root.geometry('300x200+50+50')
    root.resizable(0, 0)
    root.attributes('-topmost', 1)


    root.mainloop()

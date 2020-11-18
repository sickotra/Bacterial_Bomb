# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:21:20 2020

@author: shiva
"""

from tkinter import *

class BactBombGUI:
    
    def __init__(self, master):
        self.master = master
        
        master.title("Bacterial Bomb")
        master.geometry("1000x500")
        master.configure(background = "green")
        
        self.Title_label = Label(master, text="Bacterial Bomb - Model to Track Contamination",
                                 fg = "light green",
                                 bg = "black",
                                 font = "Helvetica 20 bold italic")
        self.Title_label.pack()
        
        
        self.logo = PhotoImage(file="jupyter_cover_image1.gif")
        self.label_1 = Label(master, image=self.logo)
        self.label_1.pack()
        
        
        
    
#---------- DELETE AFTERWARDS, use in main program --------  
root = Toplevel()

GUI = BactBombGUI(root)
root.mainloop()
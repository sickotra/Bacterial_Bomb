# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:21:20 2020

@author: shiva
"""

from tkinter import *  #import all from tkinter for the GUI

class BactBombGUI:
    
    def __init__(self, master):
        self.master = master
        
        master.title("Bacterial Bomb") #set the title, window size, bg colour
        master.geometry("1000x500")
        master.configure(background = "green")
        
        self.Title_label = Label(master,    # title text on the window
                                 text="Bacterial Bomb - Model to Track Contamination",
                                 fg = "light green",
                                 bg = "black",
                                 font = "Helvetica 20 bold italic")
        self.Title_label.pack() #add to main window
        
        
        self.logo = PhotoImage(file="jupyter_cover_image1.gif") #image to add
        self.label_1 = Label(master, image=self.logo) #label to add the image
        self.label_1.pack()
        
        
        # slider for the number of particles
        self.particle_scale = Scale(master, variable = DoubleVar(), 
                           from_=0, to=5000,  #range
                           orient = HORIZONTAL, 
                           fg = "black", #text colour
                           bg = "green", #background col
                           bd = "1.5",   #border width
                           font = "Helvetica",
                           highlightcolor = "light green",
                           sliderlength = 50,
                           length = 200,
                           label = "Number of Particles")
        self.particle_scale.pack()
        self.particle_scale.set(5000)
    

    # def select_particle_no(self, num_of_particles):
    #     selection = 
        
        
        
        
    
#---------- DELETE AFTERWARDS, use in main program --------  
root = Toplevel()

GUI = BactBombGUI(root)
root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:21:20 2020

@author: shiva
"""

from tkinter import *  #import all from tkinter for the GUI
import runpy #to run the model spread main program
import os


class BactBombGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Bacterial Bomb") #set the title, window size, bg colour
        master.geometry("1000x500")
        master.configure(background = "green")
        
    
        #title displayed on window
        self.Title_label = Label(master,    # title text on the window
                                 text="Bacterial Bomb - Model to Track Contamination",
                                 fg = "light green",
                                 bg = "black",
                                 font = "Helvetica 20 bold italic")
        self.Title_label.pack() #add to main window
        
        
        
        #image displayed on window
        self.logo = PhotoImage(file="jupyter_cover_image1.gif") #image to add
        self.label1 = Label(master, image=self.logo) #label to add the image
        self.label1.pack()
        
        
        
        #run program with defaults text & button
        self.label2 = Label(master, 
                            text = "The default parameters are:\n"
                            "Number of Particles = 5000\n Wind directions -\n"
                            " East = 75%,    West = 5%\n"
                            " North = 10%,    South = 10%",
                            font = "Helvetica 12",
                            fg = "black",
                            bg = "green",
                            highlightcolor = "white",
                            bd = "1.5")
        self.label2.place(relx=0.3, rely=0.76, anchor=CENTER)
                            
        self.default_button = Button(master,
                                     text = "Run with default parameters",
                                     font = "Helvetica 12 bold",
                                     fg = "light green",
                                     bg = "gray43",
                                     relief =RAISED,
                                     command = self.defaults) 
        self.default_button.place(relx=0.3, rely=0.89, anchor=CENTER)
        
        
        
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
        self.particle_scale.place(relx=0.7, rely=0.75, anchor=CENTER)
        
        # button to set number of particles
        self.particle_button = Button(master,
                                      font = "Helvetica 12 bold",
                                      text = "Set number of particles",
                                      fg = "light green",
                                      bg = "gray43",
                                      relief =RAISED) #command removed
        self.particle_button.place(relx=0.7, rely=0.89, anchor=CENTER)
        
        
        # exit the gui
        self.QUIT_button = Button(master,
                                  font = "Helvetica 12 bold",
                                  text="QUIT",
                                  fg="red",
                                  bg = "gray43",
                                  relief=RAISED, 
                                  command=self.Quit)
        self.QUIT_button.place(relx=0.95, rely=0.95, anchor=CENTER)
    
        # help text file    
        self.HELP_button = Button(master,
                                  font = "Helvetica 12 bold",
                                  text="HELP",
                                  fg="black",
                                  bg = "gray43",
                                  relief=RAISED, 
                                  command=self.Help)
        self.HELP_button.place(relx=0.05, rely=0.95, anchor=CENTER)
        



    def select_particle_no(self, num_of_particles):  #the func that runs when button clicked
        
        num_of_particles = int(particle_scale.get())
        return num_of_particles
    
    def defaults(self):
        runpy.run_path("model_spread.py")
        
    def Quit(self):
        root.destroy()
   
    def Help(self):
        readme = "gui_help.txt"
        os.startfile(readme)
        
        
    
# #---------- DELETE AFTERWARDS, use in main program --------  
# root = Toplevel()

# GUI = BactBombGUI(root)
# root.mainloop()
# -*- coding: utf-8 -*-
"""
Programming for Social Science - Assignment 2.
GUI Class and code to execute.

Created on Wed Nov 18 20:21:20 2020
@author: Shivani Sickotra

"""

from tkinter import *  #import all from tkinter for the GUI
import runpy #to run the model spread main program
import os #to open help file


class BactBombGUI:
    """
    BactBombGUI Class:
        A class to create the GUI for the bacterial bomb model.
        
    Constructor arguements:
        master -- the main application entry window 
        
    GUI features:
        - Button to run model_spread.py file 
        - Quit button
        - Help button
    """
    
    def __init__(self, master):
        """Construct the labels and buttons that will appear on the GUI."""
        
        self.master = master
        master.title("Bacterial Bomb") #set the title, window size, bg colour
        master.geometry("1000x500")
        master.configure(background = "green")
        
        
        # Title displayed on window
        self.Title_label = Label(master,    # title text on the window
                                 text="Bacterial Bomb - Model to Track Contamination",
                                 fg = "light green",
                                 bg = "black",
                                 font = "Helvetica 20 bold italic")
        self.Title_label.pack() #add to main window
        
        
        # Image displayed on window
        self.logo = PhotoImage(file="jupyter/logo.gif") #image to add
        self.label1 = Label(master, image=self.logo) #label to add the image
        self.label1.pack()
        
        
        # Run program with defaults
        self.label2 = Label(master, 
                            text = "The default parameters are:\n"
                            "Number of Particles = 5000\n Wind directions -\n"
                            " East = 75%,    West = 5%\n"
                            " North = 10%,    South = 10%",
                            font = "Helvetica 12",
                            fg = "black",
                            bg = "chartreuse3",
                            highlightcolor = "white",
                            bd = "1.5")
        self.label2.pack()
                            
        self.default_button = Button(master,
                                     text = "Run with default parameters",
                                     font = "Helvetica 12 bold",
                                     fg = "light green",
                                     bg = "gray43",
                                     relief =RAISED,
                                     command = self.defaults) 
        self.default_button.pack()
        
        
        # Exit the GUI
        self.QUIT_button = Button(master,
                                  font = "Helvetica 12 bold",
                                  text="QUIT",
                                  fg="red",
                                  bg = "gray43",
                                  relief=RAISED, 
                                  command=self.Quit)
        self.QUIT_button.place(relx=0.95, rely=0.95, anchor=CENTER)
    
    
        # Help text file    
        self.HELP_button = Button(master,
                                  font = "Helvetica 12 bold",
                                  text="HELP",
                                  fg="black",
                                  bg = "gray43",
                                  relief=RAISED, 
                                  command=self.Help)
        self.HELP_button.place(relx=0.05, rely=0.95, anchor=CENTER)
        
        
    def defaults(self):
        """Run the main model file."""
        runpy.run_path("model_spread.py")
        
    def Quit(self):
        """"Close the GUI window."""
        root.destroy()
   
    def Help(self):
        """Open the help text file."""
        readme = "gui_help.txt"
        os.startfile(readme)
        
        
    
# #--------------------- Display the GUI------------------------  
root = Toplevel()

GUI = BactBombGUI(root)
root.mainloop()
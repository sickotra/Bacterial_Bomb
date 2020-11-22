# -*- coding: utf-8 -*-
"""
Programming for Social Science - Assignment 2.
Bactrial Particle Class and code to execute.

Created on Mon Oct 12 15:26:42 2020
@author: Shivani Sickotra

"""

import random  #for random number generating 


class Particle:
    """
    Particle Class:
        A class to give attributes and behaviours to an abstract particle.
        
    Constructor arguements:
        town -- 2D list containing the area particles will be in.
        particles -- a list of all the particles in the town.
        y -- y coord before init method sets particles' coods.
        x -- x coord before init method sets particles' coods.
    
    Particle characteristics:
        - height
        - y coordinate
        - x coordinate 
        
    Particle behaviours:
        - spread
        - turbulence
    
    """
    
    def __init__(self, town, particles, y, x):
        """
        Construct the initial states of the bacterial particle instance object.

        Parameters
        ----------
        town : list.
            2D containing lists of row data from imported file 'wind.raster'.
        particles : list.
            2D containing lists of all the particles y,x coords.
        y : int.
            Initial y location of every particle.
        x : int.
            Initial x location of every particle.

        Returns
        -------
        Particle.

        """
        
        #the initial starting point for each particle is at the bomb location
        self._y = 150 
        self._x = 50
            
        self._town = town  #giving every agent access to the map of the town
        self._particles = particles #every particle access to 'particles' list
        self._height = 75 #all particles initial height = building height 75m 
        

    # Accessor methods to protect variables, hidden vars
    def get_y (self):
        """Divert access of y int variable to a hidden int variable."""
        return self._y
    
    def get_x (self):
        """Divert access of x int variable to a hidden int variable."""
        return self._x  
    
    def get_height(self):
        """Divert access of height int variable to a hidden int variable."""
        return self._height
    
    
    # Mutator methods to protect changed vars
    def set_y (self, value):
        """Divert mutation of y int variable to a hidden int variable."""
        self._y = value
        
    def set_x (self, value):
        """Divert mutation of x int variable to a hidden int variable."""
        self._x = value 

    def set_height(self, value):
        """Divert mutation of height int variable to a hidden int variable."""
        self._height = value
        
    # Properties - y, x property attribues and docstrings
    y = property (get_y, set_y, "The particle 'y' coord") 
    x = property (get_x, set_x, "The particle 'x' coord") 
    height = property (get_height, set_height, "The height of the building")
    
        
    def __repr__(self):
        """Make printable string version of instance objects in particles list."""
        
        return str([self._x, self._y]) #used to print initial & moved particles
       
    
    def spread(self, p_east, p_west, p_north, p_south):
        """
        Random walk particles 1 step in one of four directions, depending on
        direction probabilities assigned by user.

        Parameters
        ----------
        p_east : int.
            Variable for percentage probability of particle moving east.
        p_west : int.
            Variable for percentage probability of particle moving west.
        p_north : int.
            Variable for percentage probability of particle moving north.
        p_south : int.
            Variable for percentage probability of particle moving south.

        Returns
        -------
        None.

        """
        
        if p_east + p_west + p_north + p_south != 100 :  #prevent % over 100
            #not really needed as will have this in cmd line entry too 
            print ('Code will not run, Perecentage probs must add to 100%')
        
        else:
            chance = random.randint(1, 100) #select a random integer between 1-100 
            
            if chance <= p_east:
                self._x = self._x + 1 #move east 75% chance default or value entered
                
            elif (p_east < chance <= p_east + p_west):
                self._x = self._x - 1 #move west 5% chance default or value entered 
                
            elif (p_east + p_west < chance <= p_east + p_west + p_north):
                self._y = self._y + 1 #move north 10% chance default or value entered
            
            elif (p_east + p_west + p_north < chance <= p_east + p_west + p_north + p_south): 
                self._y = self._y - 1 #move south 10% chance default of value entered 
            
        #Town is non abstract landscape, particles cannot follow torus boundary
        #Create solid wall boundary, check if particle off edge & adjust
        if self._x < 0:   #if x, y hit 0, stop from going below 0 
            self._x = 0
        if self._y < 0:
            self._y = 0
        if self._x > 300:  #if x, y hit 299 (300x300 is town dimension),
            self._x = 300  #stop from going any higher
        if self._y > 300:
            self._y = 300
                
    
    def turbulence(self, p_rise, p_same, p_fall):
        """
        Random walk particles 1 step either up or down, depending on turbulence
        probabilities assigned by user, until all particles reach the ground.

        Parameters
        ----------
        p_rise : int.
            Variable for percentage probability of particle rising upwards.
        p_same : int.
            Variable for percentage probability of particle remaining at the 
            same level.
        p_fall : int.
            Variable for percentage probability of particle falling downwards.

        Returns
        -------
        None.

        """
        
        chance = random.randint(1, 100) #select a random integer between 1-100 
               
        if self._height >= 75: #for particles ABOVE the building height of 75m
            #particle rises, 20% default chance or value entered
            if chance <= p_rise:
                self._height = self._height + 1  
                
            #particle stays at same level, 10% chance or value entered   
            elif (p_rise < chance <= p_rise + p_same):
                self._height = self._height   
            
            #particle falls, 70% default chance of value entered    
            elif (p_rise + p_same < chance <= p_rise + p_same + p_fall):
                self._height = self._height - 1
                      
        elif (0 < self._height < 75):  #for particles BELOW the building height
            self._height = self._height - 1  #falls until hits the ground at 0m
                   
            
        
   
   
        
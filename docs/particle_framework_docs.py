# -*- coding: utf-8 -*-
"""
Programming for Social Science - Assignment 2.
Bactrial Particle Class and code to execute.

Created on Mon Oct 12 15:26:42 2020
@author: Shivani Sickotra

"""

import random  #for random number generating 

class Particle:
    
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
        self.y = 150 
        self.x = 50
            
       
        self.town = town  #giving every agent access to the map of the town
        self.toxicity = 70 #base toxicity is 70 and will increase later        #TODO
        self.particles = particles #every particle access to 'particles' list
        self.height = 75 #all particles initial height = building height 75m 
        
        
        
    def __repr__(self):
        """Make printable string version of instance objects in particles list."""
        
        return str([self.x, self.y]) #used to print initial & moved particles
       
    
    
    def spread(self, p_east, p_west, p_north, p_south):
        """
        Random walk particles 1 step in one of four directions, depending on
        direction probabilities assigned by user.

        Parameters
        ----------
        p_east : int or float.
            Variable for percentage probability of particle moving east.
        p_west : int or float.
            Variable for percentage probability of particle moving west.
        p_north : int or float.
            Variable for percentage probability of particle moving north.
        p_south : int or float.
            Variable for percentage probability of particle moving south.

        Returns
        -------
        None.

        """
        
        chance = random.randint(1, 100) #select a random integer between 1-100 
        
        if chance <= p_east:
            self.x = self.x + 1 #move east 75% chance default or value entered
            
        elif (p_east < chance <= p_east + p_west):
            self.x = self.x - 1 #move west 5% chance default or value entered 
            
        elif (p_east + p_west < chance <= p_east + p_west + p_north):
            self.y = self.y + 1 #move north 10% chance default or value entered
        
        elif (p_east + p_west + p_north < chance <= p_east + p_west + p_north + p_south): 
            self.y = self.y - 1 #move south 10% chance default of value entered 
            
        #Town is non abstract landscape, particles cannot follow torus boundary
        #Create solid wall boundary, check if particle off edge & adjust
        if self.x < 0:   #if x, y hit 0, stop from going below 0 
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > 300:  #if x, y hit 299 (300x300 is town dimension),
            self.x = 300  #stop from going any higher
        if self.y > 300:
            self.y = 300
        
            
    
    def turbulance(self, p_rise, p_same, p_fall):
        """
        Random walk particles 1 step either up or down, depending on turbulance
        probabilities assigned by user, until all particles reach the ground.

        Parameters
        ----------
        p_rise : int or float.
            Variable for percentage probability of particle rising upwards.
        p_same : int or float.
            Variable for percentage probability of particle remaining at the 
            same level.
        p_fall : int or float.
            Variable for percentage probability of particle falling downwards.

        Returns
        -------
        None.

        """
        
        chance = random.randint(1, 100) #select a random integer between 1-100 
               
        if self.height >= 75: #for particles ABOVE the building height of 75m
            #particle rises, 20% default chance or value entered
            if chance <= p_rise:
                self.height = self.height + 1  
                
            #particle stays at same level, 10% chance or value entered   
            elif (p_rise < chance <= p_rise + p_same):
                self.height = self.height   
            
            #particle falls, 70% default chance of value entered    
            elif (p_rise + p_same < chance <= p_rise + p_same + p_fall):
                self.height = self.height - 1
                      
        elif (0 < self.height < 75):  #for particles BELOW the building height
            self.height = self.height - 1  #falls until hits the ground at 0m
                   
            
               

        
   
   
        
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:26:42 2020

@author: shiva
"""
import random

class Particle:
    
    def __init__(self, town, particles, y, x):
        
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
        
        chance = random.randint(1, 100) #select a random integer between 1-100 
        
        if chance <= p_east:
            self.x = self.x + 1 #move east 75% chance default or value entered
            
        elif (p_east < chance <= p_east + p_west):
            self.x = self.x - 1 #move west 5% chance default or value entered 
            
        elif (p_east + p_west < chance <= p_east + p_west + p_north):
            self.y = self.y + 1 #move north 10% chance default or value entered
        
        elif (p_east + p_west + p_north < chance <= p_east + p_west + p_north + p_south): 
            self.y = self.y - 1 #move south 10% chance default of value entered 
            
    
    
    def turbulance(self, p_rise, p_same, p_fall):
        
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
                   
            
               

        
   
   
        
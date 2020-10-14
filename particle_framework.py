# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:26:42 2020

@author: shiva
"""
import random

class Particle:
    
    def __init__(self, town, particles, y, x):
        
        self.y = 150 #the initial starting point for each particle is at the bomb location
        self.x = 50
        
            
        #Giving every agent access to the map of the town
        self.town = town 
        #Creating a 'store' for the environment thats been eaten
        self.toxicity = 70 #base toxicity is 70 and will increase later
        self.particles = particles #giving every particle access to the 'particles' list
        
    # def spread (self, pwest, pnorth, psouth, peast):
        
    #     rand = random.random()
        
    #     if rand < pwest:
    #         self.x = self.x - 1
            
    #     elif rand < pnorth:
    #         self.y = self.y + 1
            
    #     elif rand < psouth:
    #         self.y = self.y - 1
        
    #     elif rand < peast:
    #         self.x = self.x + 1
    
    def __repr__(self):
        """Make printable string version of instance objects in agent list."""
        
        return str([self.x, self.y]) #used to print initial & moved particles
        
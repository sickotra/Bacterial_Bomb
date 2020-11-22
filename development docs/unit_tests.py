# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:42:19 2020

@author: shiva
"""

import random 

random.seed() #Not set so that different cases can be tested


def spread_test(self, p_east, p_west, p_north, p_south):
    """
    Test the spread method used in the Particle class in the main program.
    
    Procedure:
        1. Print the initial y and x coords of particle.
        2. Check directional variables entered add to 100%. If not, print error
           message.
        3. Print random int chance value.
        4. Depending on chance value, execute block to move particle and print
           this information.
        
    Verification:
        5. Console outputs to show results as expected.
        
    """
    
    _y = 150 
    print("This is the initial y coord", _y)
    _x = 50
    print("This is the initial x coord", _x)
    
    if p_east + p_west + p_north + p_south != 100 :
        print ('Code will not run, Perecentage probs must add to 100%')
    
    else: 
        #only run spread code IF the 4 direction args = 100
        chance = random.randint(1, 100) #select a random integer between 1-100 
        print("The random chance")
        print(chance)
        
        if chance <= p_east:
            _x = _x + 1 #move east 75% chance default or value entered
            print("x coord moved east 1m", _x)
            
        elif (p_east < chance <= p_east + p_west):
            _x = _x - 1 #move west 5% chance default or value entered 
            print ("x coord moved west 1m", _x)
            
        elif (p_east + p_west < chance <= p_east + p_west + p_north):
            _y = _y + 1 #move north 10% chance default or value entered
            print("y coord moved north 1m", _y)
            
        elif (p_east + p_west + p_north < chance <= p_east + p_west + p_north + p_south): 
            _y = _y - 1 #move south 10% chance default of value entered 
            print("y coord moved south 1m",_y)
     
        
                
            
spread_test(1, 5, 75, 10, 10)       # chance = 50 always with seed =0




def turbulence_test(self, p_rise, p_same, p_fall):
    _height = 75
    print("initial height", _height)
    
    chance = random.randint(1, 100) #select a random integer between 1-100 
    print ("the chance", chance)
    print ("p_rise is,",p_rise, "p_same is,",p_same, "p_fall is,",p_fall)
      
    if _height >= 75: #for particles ABOVE the building height of 75m
        #particle rises, 20% default chance or value entered
        if chance <= p_rise:
            _height = _height + 1  
            print ("particle height above 75m, moved it 1m up")
            
        #particle stays at same level, 10% chance or value entered   
        elif (p_rise < chance <= p_rise + p_same):
            _height = _height
            print ("height remained same, no change")
        
        #particle falls, 70% default chance of value entered    
        elif (p_rise + p_same < chance <= p_rise + p_same + p_fall):
            _height = _height - 1
            print("particle above 75m but dropped 1m")
                  
    elif (0 < _height < 75):  #for particles BELOW the building height
        _height = _height - 1  #falls until hits the ground at 0m
        print ("below building height, fall 1m")

    print ("the new height,", _height)
#turbulence_test(1, 20, 10, 70)        
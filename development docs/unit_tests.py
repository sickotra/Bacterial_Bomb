# -*- coding: utf-8 -*-
"""
Programming for Social Science - Assignment 2.
Testing for the Particle class methods.

Created on Fri Oct 16 09:38:12 2020  
@author: Shivani Sickotra

"""

import random 

random.seed() #Not set so that different cases can be tested, set to 0 to match
              #example inputs/outputs in unit_testing.docx table.

def __init__test(self, town, particles, y, x):
    """
    Test the constructor method used in the Particles class to create each
    Particle object instance.
    
    Procedure:
        1. Print the initial y and x coords of particle.
        2. Print the town data that has been passed in as an argument.
        3. Print the particle data that has been passed in as an argument.
        4. Print the height assigned to the particle.
        
    Verification:
        5. Console outputs to show results as expected.
        
    """
          
    #the initial starting point for each particle is at the bomb location
    _y = 150 
    _x = 50
    print ("The initial x and y coords of particle:", (_x, _y))
    
    _town = town  #giving every agent access to the map of the town
    print (_town) #print to confirm arg passed in 
    
    _particles = particles #every particle access to 'particles' list
    print(_particles) 
    
    _height = 75 #all particles initial height = building height 75m 
    print ("the height of the particle",_height)


town = "the town info" #arg inputs representing arg inputs in the main program
particles = "the other particles' info" 
y = 150 
x = 50
__init__test(1, town, particles, y, x)



def spread_test(self, p_east, p_west, p_north, p_south):
    """
    Test the spread method used in the Particle class in the main program.
    
    Procedure:
        1. Print the initial y and x coords of particle.
        2. Check directional variables entered add to 100%. If not, print error.
           message.
        3. Print random int chance value.
        4. Depending on chance value, execute block to move particle and print
           this information.
        
    Verification:
        5. Console outputs to show results as expected.
        
    """
    
    _y = 150 #have initial coords so can make a comparison
    print("This is the initial y coord", _y)
    _x = 50
    print("This is the initial x coord", _x)
    
    if p_east + p_west + p_north + p_south != 100 :  #prevent 100% over 100
        print ('Code will not run, Perecentage probs must add to 100%')
    
    else: 
        #only run spread code IF the 4 direction args = 100
        chance = random.randint(1, 100) #select a random integer between 1-100 
        print("The random chance: ", chance)  #chance to determine if working 
        
        if chance <= p_east:
            _x = _x + 1 #move east 75% chance default or value entered
            print("x coord moved east 1m: ", _x) #print to see what is happening
            
        elif (p_east < chance <= p_east + p_west):
            _x = _x - 1 #move west 5% chance default or value entered 
            print ("x coord moved west 1m: ", _x)
            
        elif (p_east + p_west < chance <= p_east + p_west + p_north):
            _y = _y + 1 #move north 10% chance default or value entered
            print("y coord moved north 1m: ", _y)
            
        elif (p_east + p_west + p_north < chance <= p_east + p_west + p_north + p_south): 
            _y = _y - 1 #move south 10% chance default of value entered 
            print("y coord moved south 1m: ", _y)
             
# spread_test (1, 5, 75, 10, 10)  #DEFAULTS
spread_test (1, 30, 40, 20, 10) # some inputs to test, self = 1 (Particle)
spread_test(1, 50, 50, 50, 50)  # some inputs to test sum to 100% cond works



def turbulence_test(self, p_rise, p_same, p_fall):
    """
    Test the turbulence method used in the Particle class in the main program.
    
    Procedure:
        1. Print the initial height of particle.
        3. Print random int chance value and turbulence probs.
        3. Depending on the height, execute block to move particle and print
           this information.
        4. Print new height of particle.      
        
    Verification:
        5. Console outputs to show results as expected.
        
    """
    
    _height = 75
    print("Initial particle height: ", _height) #initial height to compare
    
    chance = random.randint(1, 100) #select a random integer between 1-100 
    print ("The random chance: ", chance)
    print ("p_rise is:",p_rise, " p_same is:",p_same, " p_fall is:",p_fall)
      
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
            print("particle above 75m, but dropped 1m")
                  
    elif (0 < _height < 75):  #for particles BELOW the building height
        _height = _height - 1  #falls until hits the ground at 0m
        print ("below building height, fall 1m")

    print ("the new particle height:", _height) #new updated height to compare
    
turbulence_test(1, 20, 10, 70) #the turb probs are always the same, hardcoded.  
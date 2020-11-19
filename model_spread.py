# -*- coding: utf-8 -*-
"""
Programming for Social Science - Assignment 2.
Bacterial Spread Model.

Created on Sat Oct 10 11:40:25 2020
@author: Shivani Sickotra

"""

# Import packages needed to run
import csv #to allow raster data to be read
import random   #for random number generating
import matplotlib.pyplot as plt #for plotting spread 
import particle_framework #the particle class created 
import pandas as pd #for density map data frame
import seaborn as sns #for creating density map 
import time  #to time spreading of particles
import bact_bomb_gui as gui
from tkinter import *

#num_of_particles = 5000

#'fix' the random numbers so outputs stay constant, can change the seed arg
random.seed(0)



# Setting up town and identifying bombing location 
f = open ('wind.raster', newline='') #read in data from raster file
#csv.reader gives data as list of list to be looped through
dataset = csv.reader (f, quoting=csv.QUOTE_NONNUMERIC) #converts no. to floats

town = [] #empty town list to add the rowlist elements (mutable)

for row in dataset:
    rowlist = [] #empty list to add each row as an element
    for value in row:
        rowlist.append (value) #adds each row's data as its own rowlist element
    town.append (rowlist)  #each rowlist added to environ list, 2D now 
f.close() 	#file closed after reading data



# Locating the bomb detonation point
counter = 0 #start a counter for the rows in the town list
for row in town: #both for loops to check through every value in the 2D list
    for value in row:
        if value != 0: #if the value is not equal to zero, then set bomb coords 
            bomb_x = row.index(value) #bomb x coord
            bomb_y = counter 
            #will print the coord of the only non zero pixel value (255)
            print("Coords of the building where bomb detonated:",(bomb_x, bomb_y))
    #step the row counter by 1 to loop through all rows until non zero found
    counter += 1



# Plotting the raster data
plt.ylim (0, 300) #setting graph axis 300x300 to match raster
plt.xlim (0, 300)
plt.title ('A plot to show the map of the town and the bombing location')
plt.xlabel('x metres') #graph axis labels, 1 pixel = 1 metre
plt.ylabel('y metres')
#mark the bomb location with a red diamond overlay 
plt.scatter (50, 150, color='red', marker=('D'))
#plotting map of the area/town and bombing location
plt.imshow(town) 




# Major model parameters
num_of_particles = 5000

#Chances/probability of wind blowing particle in different directions
p_east = 75  #75 means 75% chance particle moves east each second/iteration 
p_west = 5   #NESW probs can be integer or decimal/float, but will only use int
p_north = 10 #just need sum = 100
p_south = 10

#Chances of wind turbulance effects 
p_rise = 20 #20% chance particle rises 1m per second (1 pixel per iteration)
p_same = 10 #particle stays at the same level
p_fall = 70 #use integers, just need sum = 100




particles = [] #empty list to add Partical class instances

print ("Initialising particles--") 
# Creating particles and adding to particles list

for i in range(num_of_particles): 
    y = 150
    x = 50
    #passing in data from town & particles list and y,x and appending to list
    particles.append (particle_framework.Particle(town, particles, y, x)) 
    #TEST to see each part get part list, all the same starting point!
    #print (particles[i].particles)  
#print ("Initial particles:") #comment out for large no's of agents, TEST
#print (particles) #prints list of all initial agents at (50,150) bomb location



print ("Spreading bomb particles--")
# Particles spread across town either NESW directions and rise/fall 
start = time.perf_counter() #start clock to assess efficiency 
    
#Methods in Particles class act on every element in particles list
for i in range (num_of_particles): 
    
    #only run methods when the height of the particle is not 0 ie. not on ground
    seconds_count = 0 #to count the no of seconds/times while loop runs
    while particles[i].height != 0:
        
        seconds_count += 1 #increment by 1 every loop iteration, 1 iter = 1 sec
        particles[i].spread(p_east, p_west, p_north, p_south) #NESW movement
        particles[i].turbulance(p_rise, p_same, p_fall) #up/down movement
    #print (particles[i].height) #TEST to see turbulance method working
#print("Particles after spreading:") #comment out for large no's of particles
#print (particles) # 2D list/array of particles at their end locations, TEST 

end = time.perf_counter() #end the timer for the calculating distances loops
print ("All particles have now settled on the ground")
print ("Time taken to calculate particles reaching ground = " + str (end - start))
print ("Time taken for particles to actually hit the ground in the town = "+str(seconds_count)+" seconds")


# Plotting all particles after spreading on a scatter plot
for i in range (num_of_particles):
    #ith obj from particles list, using Particles Class to specify x, y coords
    plt.scatter (particles[i].x, particles[i].y) 
#figure caption
txt= "Fig 1. End locations of "+str(num_of_particles)+" particles in the town after "+str(seconds_count)+" seconds"
plt.figtext(0.5, 0.001, txt, wrap=True, horizontalalignment='center', fontsize=10)
plt.show() 


# Outputting end locations of all particles, after stepping, as a text file
f = open("outputs/end_locations.txt",'w', newline='') #builtin open func to write end coords
for line in particles: #for every line in particles list
    f.write (repr(line)) #write as a string in the text file
f.close() #file closed after writting the coords




# Creating separate lists for all x & y end locations for density plot
all_x_data = []  #empty list for all x and y coords to go into
all_y_data = [] 
for i in range (num_of_particles):
    #for every particle, add its corresponding x coord/y coord into the list 
    all_x_data.append (particles[i].x)
    all_y_data.append (particles[i].y)
#print(all_x_data)   #to test that the x & y coords list is made correctly
#print(all_y_data)



# Creating dictionary for x, y coords to use as pandas dataframe for density plot
d = {'x': all_x_data,'y': all_y_data} #creating the dictionary of 2 columns 

# Create pandas data frame from the dict and output density map
df = pd.DataFrame(d) #can check by calling d & df in console

plt.figure() #create a 2nd figure output
plt.title ('Density map of ' +str(num_of_particles)+' bacterial particles')
plt.xlabel('x metres') #graph axis labels, 1 pixel = 1 metre
plt.ylabel('y metres')


# Density plot using seaborn, darker green = very dense, yellow = less dense
density = sns.kdeplot(x= df.x, y= df.y, cmap='YlGn',shade=True,bw_method=0.5) 
density.figure.savefig("outputs/density_map.png") #save as an image file




# Save density map to file as text
for i in range (num_of_particles):  #for every particle
    #for every particles y, x coords in the town, add 1 to the town pixel.
    #the town pixel values will represent the no of particles/density there
    town[particles[i].y][particles[i].x] += 1 

f = open('outputs/density_map_text.txt', 'w', newline='') #create new text file
writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#for every row in the town list, write that row to the new txt file
for line in town:
    writer.writerow(line) 
f.close() #close the file

# The output text file will have 0's where no particles are present,
# and e.g a pixel value of 20 when 20 particles are present,density is retained      

#--------------------------UNCOMMENT AT THE END--------------------------------
#Call GUI class
root = Toplevel() #the main window
GUI = gui.BactBombGUI(root) #from gui module use method
root.mainloop() #run the code



# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:40:25 2020

@author: shiva
"""
import csv #to allow raster data to be read
import random   #for random number generating
import matplotlib.pyplot as plt #for plotting spread 
import particle_framework #the particle class created 
# import numpy as np #for plotting density?
# from scipy.stats import gaussian_kde
# import seaborn as sns
# import pandas as pd



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
print ("Coords of building where bomb detonated: (50, 150)") #rounded to int



# Major model parameters
# TODO ALLOW ADJUSTMENT FROM CMD PROMPT OR JUPYTER NOTEBOOK
num_of_particles = 10
num_of_iterations = 100 #i.e after 700 seconds, 11mins

#Chances/probability of wind blowing particle in different directions
p_east = 75  #75 means 75% chance particle moves east each second/iteration 
p_west = 5
p_north = 10
p_south = 10

#Chances of wind turbulance effects 
p_rise = 20 #20% chance particle rises 1m per second (1 pixel per iteration)
p_same = 10 #particle stays at the same level
p_fall = 70



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
#print ("Initial particles:") #comment out for large no's of agents
#print (particles) #prints list of all initial agents at (50,150) bomb location




print ("Spreading bomb particles--")
# Particles spread across town either NESW directions and rise/fall 

for j in range (num_of_iterations):   #moves the coords num of iteration times
    #randomly shuffle particles list each iternation to reduce model artifacts
    random.shuffle (particles) 
    #methods in Particles class act on every element in particles list
    for i in range (num_of_particles): 
        particles[i].spread(p_east, p_west, p_north, p_south) #NESW movement
        particles[i].turbulance(p_rise, p_same, p_fall) #up/down movement
        #print (particles[i].height) #test to see turbulance method working
#print("Particles after spreading:") #comment out for large no's of particles
print (particles) # 2D list/array of particles at their end locations 


# Plotting all particles after spreading on a scatter plot
for i in range (num_of_particles):
    #ith obj from particles list, using Particles Class to specify x, y coords
    plt.scatter (particles[i].x, particles[i].y) 
plt.show() 


# Outputting end locations of all particles, after stepping, as a text file
f = open("particles_end.txt",'w', newline='') #builtin open func to write end coords
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
d = {'x': all_x_data,'y': all_y_data}  #creating the dictionary of 2 columns, call d in console to check dict made correctly

#create pandas data frame from the dict



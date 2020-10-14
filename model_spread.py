# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:40:25 2020

@author: shiva
"""
import csv #to allow raster data to be read
import matplotlib.pyplot #for plotting spread 
import particle_framework #the particle class created 
import random   #for random number generating



#Setting up town and to identify bombing location 
f = open ('wind.raster', newline='') #read data from raster file
#csv.reader gives data as list of list to be looped through
dataset = csv.reader (f, quoting=csv.QUOTE_NONNUMERIC) #convers no. to floats

town = [] #empty list to add the rowlist elements (mutable)

for row in dataset:
    rowlist = [] #empty list to add each row as an element
    for value in row:
        rowlist.append (value) #adds each row's data as its own rowlist element
    town.append (rowlist)  #each rowlist added to environ list, 2D now 
f.close() 	#file closed after reading data

#Plotting the raster data
matplotlib.pyplot.ylim (0, 300) #setting graph axis
matplotlib.pyplot.xlim (0, 300)
matplotlib.pyplot.title ('A plot to show the map of the town and the bombing location')
matplotlib.pyplot.xlabel('x') #graph axis labels
matplotlib.pyplot.ylabel('y')
#mark the bomb location with a red diamond overlay 
matplotlib.pyplot.scatter (50, 150, color='red', marker=('D'))
#plotting map of the area/town and bombing location
matplotlib.pyplot.imshow(town) 
print ("Coords of building where bomb detonated: (50, 150)" ) #rounded to nearest int





#major model params
# pwest = 0.05 #probs of wind blowing particle
# pnorth = 0.1
# psouth = 0.1
# peast = 0.75
num_of_particles = 5000
num_of_iterations = 100
#current_wind = ???


particles = []

print ("Initialising particles--") 
# Creating particles and adding to particles list

for i in range(num_of_particles): 
    y = 150
    x = 50
    #passing in data from town & particles list and y,x 
    particles.append (particle_framework.Particle(town, particles, y, x)) 
    #print (particles[i].particles)  #TEST to see each part get part list, all the same starting point!
#print ("Initial agents:") #comment out for large no's of agents
#print (particles)  #prints list of all initial agents to see list is made correctly, all same starting point as the bomb location





#TEST IF WIND PROBABILITIES ARE WORKING
#print(particles[1])
#print (chance)



print ("Spreading bomb particles--")
for j in range (num_of_iterations):   #moves the coords num of iteration times
    #randomly shuffles agents list each iternation, reduce model artifacts
    #random.shuffle (agents) 
    for i in range (num_of_particles): #funcs act on every element in particles list
        particles[i].spread() #caling spread func in Particles class 
    
print("Particles after moving:") #comment out for large no's of particles
print (particles) # 2D list of particles after stepping


#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_particles):
    #get ith obj from particles list, using Particles Class to specify x, y coords
    matplotlib.pyplot.scatter (particles[i].x, particles[i].y) 
matplotlib.pyplot.show() 

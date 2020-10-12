# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:40:25 2020

@author: shiva
"""
import csv #to allow raster data to be read
import matplotlib.pyplot #for plotting spread 



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
#plotting map of the area/town and bombing location
matplotlib.pyplot.imshow(town) 

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:27:06 2020

@author: shiva
"""

from distutils.core import setup # to set up executable
import py2exe  #to convert py file to exe

#setup single console application, main entry is gui file.
setup(console=['bact_bomb_gui.py'])  

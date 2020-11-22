# Bacterial_Bomb

A Model to track the spread of bacterial particles in a town.
The document `./development docs/supporting_info` has full details of how the program works
and its features. 

## Main folder Contents:
* `README.md`- This file outlining folder contents and where to find more information on the program
* `LICENSE` - GNU General Public License, version 3 (GPLv3)
* `bact_bomb_gui.py` - The main file to be run
* `model.py` - Code for the main class in the program
* `particle_framework.py` - Contains particles' behaviours class
* `gui_help.txt` - File that includes help for the GUI Help button
* `BactBomb_sickotra.ipynb` - Jupyter notebook file 

## Subfolders Contents:
* inputs:
	* `wind.raster` - the town data
* outputs:
	* `density_map.png` - image output of density plot
	* `density_map_text.txt` - text output of density plot
	* `end_locations.txt` - end coords of particles
* jupyter:
	* `initial_town.png` - image to be used in the notebook
	* `logo.gif` - gif to be used as a logo in the notebook and GUI
	* `town_after_spread.png` - image to be used in the notebook
* development docs:
	* `supporting_info.pdf` - PDF explaining program in detail 
	* `UML.pdf` - UML class diagram
	* `UML.XML` - XML format to allow editing 
	* `unit_tests.py` - tests for class method units
* docs:
	* folder to contain the code and links for sphinx docstrings pages 


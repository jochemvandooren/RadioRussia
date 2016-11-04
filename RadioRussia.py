# -*- coding: utf-8 -*-
"""
Radio Russia
"""

#loading the dictionary from with pickle
import pickle
with open('Ukraine.pickle', 'rb') as handle:
  ukraine = pickle.load(handle)

towers = ['A','B','C','D','E','F','G']
towerdict = {}

def calculate_towers(): 
	#loop through all the provinces      
    for province in ukraine:
        towers2 = ['A','B','C','D','E','F','G']
        neighbours = ukraine[province]

        #remove possible towers based on neighbours
        for neighbour in neighbours:
            if neighbour in towerdict.keys():
                if towerdict[neighbour] in towers2:
                    towers2.remove(towerdict[neighbour])
    
        #get first tower from list    
        towerdict[province] = towers2[0]
                
    return towerdict
        
       
print calculate_towers()
            

    
# -*- coding: utf-8 -*-
"""
Radio Russia
"""
from random import shuffle

#loading the dictionary from with pickle
import pickle
with open('ukraine_dictionary.pickle', 'rb') as handle:
  ukraine = pickle.load(handle)

print ukraine

towers = ['A','B','C','D','E','F','G']
towerdict = {}
indices = range(1,len(ukraine)+1)



def calculate_towers(indices): 
    shuffle(indices)
	#loop through all the provinces      
    for i in indices:
        towers2 = ['A','B','C','D','E','F','G']
        neighbours = ukraine[i]

        #remove possible towers based on neighbours
        for neighbour in neighbours:
            if neighbour in towerdict.keys():
                if towerdict[neighbour] in towers2:
                    towers2.remove(towerdict[neighbour])
    
        #get first tower from list    
        towerdict[i] = towers2[0]
                
    return towerdict
print calculate_towers(indices)

colours = {'A': '#7F0000', 'B':'#FF4C4C','C': '#FF0000','D':'#7F2626', 'E':'#CC0000'}
            


import xml.etree.ElementTree as ET
tree = ET.parse('ua.svg')
root = tree.getroot()
for province in root[2]:
	province.set('fill', colours[towerdict[int(province.attrib['id'])]])

tree.write('output.svg')

#TEST TO CHECK IF MORE THAN 3 TOWERS
# for i in range(0,200):
# 	if 'D' not in calculate_towers(indices).values():
# 		print 'SICK'
        
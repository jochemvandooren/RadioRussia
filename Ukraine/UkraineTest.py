# -*- coding: utf-8 -*-
"""
Radio Russia
"""
from random import shuffle

#loading the dictionary from with pickle
import pickle
with open('Ukraine.pickle', 'rb') as handle:
  ukraine = pickle.load(handle)


towers = ['A','B','C','D','E','F','G']
indices = range(1,len(ukraine)+1)
n = 0
solution = []
shuffle(indices)

def calculate_towers(indices, solution, towerdict):
    if len(towerdict) == 27:
        return towerdict

    #loop through all the provinces
    for i in indices:
        if i not in solution:
            towers2 = ['A','B','C','D','E','F','G']
            neighbours = ukraine[i]

            #print solution
            #remove possible towers based on neighbours
            for neighbour in neighbours:
                if neighbour in towerdict:
                    if towerdict[neighbour] in towers2:
                        towers2.remove(towerdict[neighbour])

            if towers2[0] in ['A', 'B', 'C', 'D']:
                towerdict[i] = towers2[0]
                result = calculate_towers(indices, solution + [i], towerdict)
                if result != None:
                    return result
                del towerdict[i]

    return None

calculate_towers(indices, solution, {})
#colours = {'A': '#7F0000', 'B':'#FF4C4C','C': '#FF0000','D':'#7F2626', 'E':'#CC0000'}



#import xml.etree.ElementTree as ET
#tree = ET.parse('Ukraine.svg')
#root = tree.getroot()
#for province in root[2]:
#	province.set('fill', colours[towerdict[int(province.attrib['id'])]])

#tree.write('output.svg')

#TEST TO CHECK IF MORE THAN 3 TOWERS
# for i in range(0,200):
# 	if 'D' not in calculate_towers(indices).values():
# 		print 'SICK'

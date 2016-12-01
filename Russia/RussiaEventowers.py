# -*- coding: utf-8 -*-
"""
Radio Russia
"""
from random import shuffle
from collections import Counter
import time
import csv
import random

#loading the dictionary from with pickle
import pickle
with open('Russia.pickle', 'rb') as handle:
  ukraine = pickle.load(handle)

ukraine[31].append(34)


towers = ['A','B','C','D','E','F','G']
indices = range(1,len(ukraine)+1)
n = 0
solution = []


towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
shuffle(indices)

def calculate_towers(indices, solution, towerdict):
    if len(towerdict) == len(ukraine):
        return towerdict

    if time.time() - start > 0.3:
    	towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
        for x in towerdict:
            towercounts[towerdict[x]] += 1
        print towercounts
        print solution
    	return towerdict

    optionsdict = {}

    for province in ukraine:
    	if province not in towerdict:
	    	towers2 = ['A','B','C','D','E','F','G']
	    	for neighbour in ukraine[province]:
	            if neighbour in towerdict:
	                if towerdict[neighbour] in towers2:
	                    towers2.remove(towerdict[neighbour])
	        optionsdict[province] = len(towers2)




    startwith = random.choice([k for k,v in optionsdict.iteritems() if v == min(optionsdict.values())])


    indices.remove(startwith)
    indices.insert(0, startwith)
    print len(solution)

    #loop through all the provinces
    for i in indices:
        if i not in solution:
            towers2 = ['A','B','C','D','E','F','G']
            neighbours = ukraine[i]



            towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
            for x in towerdict:
            	towercounts[towerdict[x]] += 1


            towers2 = sorted(sorted(towercounts), key=towercounts.get, reverse=False)+['E', 'F', 'G']

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
                    print towercounts
                    return result
                del towerdict[i]

    return None

start = time.time()
x = calculate_towers(indices, solution, {})

# for i in range(100):
#     shuffle(indices)
#     start = time.time()
#     output = open('results.csv', 'a')
#     result = calculate_towers(indices, solution, {})
#     towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
#     if result:
#         for x in result:
#             towercounts[result[x]] += 1
#     result = str(result)

#     if result != 'None':
#     	print 'KLAAR'
#     	output.write(result+str(towercounts))
#         output.write('\n')
#     	break

colours = {'A': '#7F0000', 'B':'#FF4C4C','C': '#FF0000','D':'#7F2626', 'E':'#CC0000'}



import xml.etree.ElementTree as ET
tree = ET.parse('Russia.svg')
root = tree.getroot()
for province in root[1]:
	province.set('fill','black')
for province in root[1]:
	try:
	    province.set('fill', colours[x[int(province.attrib['id'])]])
	except:
		pass

tree.write('output.svg')



# -*- coding: utf-8 -*-
"""
Radio Russia
This file contains an algorithm that colours SVG's where every colour is used the same amount of times
On line 92 you can change the country string. Choose 'USA', 'China', 'Ukraine' or 'Russia'.
"""
from random import shuffle
from collections import Counter
import time
import csv
import random
import pickle
import xml.etree.ElementTree as ET

def loadDict(country):
    file = country+'.pickle'

    with open(file, 'rb') as handle:
      country_dict = pickle.load(handle)

    #some dictionaries have to be fixed
    if len(country_dict) == 48:
        country_dict[43].append(41)
        country_dict[29].append(36)
    if len(country_dict) == 31:
        country_dict[3].append(1)

    return country_dict

towers = ['A','B','C','D','E','F','G']
solution = []

def calculate_towers(indices, solution, towerdict):
    if len(towerdict) == len(country):
        return towerdict
    
    #algorithm has to stop after certain amount of time
    if time.time() - start > .3:
    	towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
        for x in towerdict:
            towercounts[towerdict[x]] += 1
    	return towerdict


    #choose next province with least amount of possible towers left
    optionsdict = {}
    for province in country:
    	if province not in towerdict:
	    	towers2 = ['A','B','C','D','E','F','G']
	    	for neighbour in country[province]:
	            if neighbour in towerdict:
	                if towerdict[neighbour] in towers2:
	                    towers2.remove(towerdict[neighbour])
	        optionsdict[province] = len(towers2)
    startwith = random.choice([k for k,v in optionsdict.iteritems() if v == min(optionsdict.values())])
    indices.remove(startwith)
    indices.insert(0, startwith)


    #loop through all the provinces
    for province in indices:
        if province not in solution:
            towers2 = ['A','B','C','D','E','F','G']
            neighbours = country[province]

            #sort towers2 to have the least used tower be the first index
            towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
            for x in towerdict:
            	towercounts[towerdict[x]] += 1
            towers2 = sorted(sorted(towercounts), key=towercounts.get, reverse=False)+['E', 'F', 'G']


            #remove possible towers based on neighbours
            for neighbour in neighbours:
                if neighbour in towerdict:
                    if towerdict[neighbour] in towers2:
                        towers2.remove(towerdict[neighbour])


            if towers2[0] in ['A', 'B', 'C', 'D']:
                towerdict[province] = towers2[0]
                result = calculate_towers(indices, solution + [province], towerdict)
                if result != None:

                    return result
                del towerdict[province]
    return None


start = time.time()
#change this variable to change the country
country_string = 'Russia'
country = loadDict(country_string)
indices = range(1,len(country)+1)
result = {}
result = calculate_towers(indices, [], {})
for y in range(0,100):
    shuffle(indices)
    start = time.time()
    result = calculate_towers(indices, [], {})

    if len(result) == len(country):
        towers_result = []
        for z in result:
            if result[z] not in towers_result:
                towers_result.append(result[z])
        if len(towers_result) == 4:
            print y+1, 'simulation(s) made in order to find a solution with 4 towers.'
        break

print 'These are the provinces with the assigned towers for the country', country_string
print result

print
print 'The amount of towers used is:',len(towers_result)
towercounts = {'A':0, 'B':0, 'C':0, 'D':0}
for x in result:
    towercounts[result[x]] += 1
print towercounts
print 




#ALL ABOUT THE COLOURING OF THE SVG
colours = {'A': '#e41a1c', 'B':'#377eb8','C': '#4daf4a','D':'#984ea3', 'E':'#ff7f00', 'F':'#ffff33', 'G': '#a65628'}
tree = ET.parse(country_string+'.svg')
root = tree.getroot()

#ukraine has a different SVG than the others!
if country_string == 'Ukraine':
    index = 2
else:
    index = 1

for province in root[index]:
    province.set('fill','black')
for province in root[index]:
    try:
        province.set('fill', colours[result[int(province.attrib['id'])]])
    except:
        pass
tree.write(country_string+'_output.svg')
print 'Open',country_string+'_output.svg','to see the result!'







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





# -*- coding: utf-8 -*-
"""
Radio Russia
Greedy algorithm to colour different SVG's
On line 65 you can change the country string. Choose 'USA', 'China', 'Ukraine' or 'Russia'.
"""
from random import shuffle
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
towerdict = {}

def calculate_towers(indices): 
    shuffle(indices)

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
    for i in indices:
        towers2 = ['A','B','C','D','E','F','G']
        neighbours = country[i]

        #remove possible towers based on neighbours
        for neighbour in neighbours:
            if neighbour in towerdict.keys():
                if towerdict[neighbour] in towers2:
                    towers2.remove(towerdict[neighbour])
    
        #get first tower from list    
        towerdict[i] = towers2[0]
                
    return towerdict

#This is where you can change the country
country_string = 'USA'
country = loadDict(country_string)

#Make simulations until there is a result with only 4 different towers
for x in range(1,10000):
    towerdict = {}
    indices = range(1,len(country)+1)
    shuffle(indices)
    result = calculate_towers(indices)
    
    towers_result = []
    for y in result:
        if result[y] not in towers_result:
            towers_result.append(result[y])
    if len(towers_result) == 4:
        print x, 'simulation(s) made in order to find a solution with 4 towers'
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



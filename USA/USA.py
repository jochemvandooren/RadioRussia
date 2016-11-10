import pickle

with open('USA.pickle', 'rb') as handle:
  USA = pickle.load(handle)

print USA
from random import shuffle


towers = ['A','B','C','D','E','F','G']
colours = {'A': '#7F0000', 'B':'#FF4C4C','C': '#FF0000','D':'#7F2626', 'E':'#CC0000', 'F':'green', 'G':'blue'}
towerdict = {}
indices = range(1,len(USA)+1)

def calculate_towers(indices): 
    shuffle(indices)
	#loop through all the provinces      
    for i in indices:
        towers2 = ['A','B','C','D','E','F','G']
        neighbours = USA[i]

        if len(neighbours) == 0:
        	towerdict[i] = towers2[0]
        else:

	        #remove possible towers based on neighbours
	        for neighbour in neighbours:
	            if neighbour in towerdict.keys():
	                if towerdict[neighbour] in towers2:
	                    towers2.remove(towerdict[neighbour])
	    
	        #get first tower from list    
	        towerdict[i] = towers2[0]
                
    return towerdict
    
print calculate_towers(indices)

import xml.etree.ElementTree as ET
tree = ET.parse('USA.svg')
root = tree.getroot()
for province in root[1]:
	province.set('fill', colours[towerdict[int(province.attrib['id'])]])

tree.write('output.svg')
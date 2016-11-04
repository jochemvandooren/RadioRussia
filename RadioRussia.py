# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 13:36:18 2016

@author: Jochem
"""

ukraine = {1:[2,3], 2:[1,3,5,6,7], 3:[1,2,4,5], 4:[3,5,8,10], 5:[2,3,4,7,8], 6:[2,7], 
           7:[2,5,6,8,9], 8:[4,5,7,9,10], 9:[7,8,10,14], 10:[4,8,9,11,14,15,16],
          11:[10,13,16], 12:[14], 13:[11,16,17,20], 14:[9,10,15,21,22,12], 15:[10,14,16,21],
          16:[10,11,13,15,20,21], 17:[13,18,19,20], 18:[17], 19:[17,20,25], 20:[13,16,17,19,21,24,25],
          21:[14,15,16,20,22,23,24], 22:[14,21,23], 23:[21,22,24], 24:[20,21,23,25,26], 25:[19,20,24,26],
          26:[24,25]}


          
towers = ['A','B','C','D','E','F','G']

towerdict = {}

def calculate_towers(starting_province): 
    n = len(ukraine)
    
      
    for province in ukraine:
        print province
        towers2 = ['A','B','C','D','E','F','G']
        neighbours = ukraine[province]
    
        for neighbour in neighbours:
            if neighbour in towerdict.keys():
                if towerdict[neighbour] in towers2:
                    towers2.remove(towerdict[neighbour])
    
            
        towerdict[province] = towers2[0]
                
        print towerdict
        
    
        
def calculate_towers2(starting_province): 
    n = len(ukraine)
    
      
    for i in range (n, len(ukraine)):
        province = ukraine.keys()[i]
        neighbours = ukraine.values()[i]
        
        print province
        print neighbours
        
        towers2 = ['A','B','C','D','E','F','G']
        neighbours = ukraine[province]
    
        for neighbour in neighbours:
            if neighbour in towerdict.keys():
                if towerdict[neighbour] in towers2:
                    towers2.remove(towerdict[neighbour])
    
            
        towerdict[province] = towers2[0]
                
        print towerdict            
    
            
print calculate_towers('o')
            

    
import pickle
from random import shuffle
with open('Russia_center.pickle', 'rb') as handle:
  Russia_center = pickle.load(handle)
with open('Russia_south.pickle', 'rb') as handle:
  Russia_south = pickle.load(handle)
with open('Russia_east.pickle', 'rb') as handle:
  Russia_east = pickle.load(handle)

print Russia_east

# towers = ['A','B','C','D','E','F','G']
colours = {1: '#7F0000', 2:'#FF4C4C', 3: '#FF0000', 4:'#7F2626', 5:'#CC0000', 6:'green', 7:'blue'}
towerdict = {12: 1, 13: 2, }
# indices = range(14,len(Russia)+1)
all_options = 0

# Determine what state to color by calculating the sum of values of already coloured neighbours.
# Takes a dictionary representing a (part of a) country and returns a key representing a state.
def calculate_next(part_of_Russia): 
	#loop through all the provinces to determine next 
	check = 0
	for key in part_of_Russia:
		towers2 = [1,2,3,4,5,6,7]
		neighbours = part_of_Russia[key]

		# keep track of value
		weight = 0
		options = 4

		# choose state directly if no neighbours
		if len(neighbours) == 0:
			next = key
			
			#remove possible values based on neighbours
		else:
			for neighbour in neighbours:
				if neighbour in towerdict.keys():
					weight += towerdict[neighbour]
					options -= 1
		# save in check if highest value
		if weight > check:
			check = weight
			next = key
		print key, options
	return next

# Fills the next state. Takes a dictionary and a key-value 
def fill_next(part_of_Russia, next):

	towers2 = [1,2,3,4,5,6,7]
	neighbours = part_of_Russia[next]

	if len(neighbours) == 0:
		towerdict[next] = towers2[0]
	else:

		#remove possible towers based on neighbours
		for neighbour in neighbours:
			if neighbour in towerdict.keys():
				if towerdict[neighbour] in towers2:
					towers2.remove(towerdict[neighbour])
	
		#get first tower from list    
		towerdict[next] = towers2[0]
	# take filled state out of dictionary
	del part_of_Russia[next]
					
	

while any(Russia_center):
	next = calculate_next(Russia_center)
	fill_next(Russia_center, next)

print towerdict

while any(Russia_south):
	next = calculate_next(Russia_south)
	fill_next(Russia_south, next)

print towerdict

print calculate_next(Russia_east)

while any(Russia_east):
	next = calculate_next(Russia_east)
	fill_next(Russia_east, next)

print towerdict






import xml.etree.ElementTree as ET
tree = ET.parse('Russia.svg')
root = tree.getroot()
print root[1]
for province in root[1]:
	province.set('fill', colours[towerdict[int(province.attrib['id'])]])

tree.write('output.svg')


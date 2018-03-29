import re
import time
import sys


#reduction from 21496 to 7491


def createSet(file_name):

	ingr_set = set()

	with open(file_name, 'r') as f:
		
		for line in f:
			processed = line.strip()
			processed = processed.lower()
			ingr_set.add(processed)
	return ingr_set


def createNewFile(file_name, ingr_set):

	with open(file_name, 'w') as f:
		line_index = 0	
		for line in ingr_set:
			f.write(str(line_index)+'<!><!><!>'+line+'\n')
			line_index += 1


old_file = 'ingr_df.txt'
ingr_set = createSet(old_file)
new_file = 'reduced_ingr_df.txt'
createNewFile(new_file, ingr_set)
print('done')

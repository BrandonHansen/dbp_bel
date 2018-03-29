import re
import time
import sys


exp_name = True
exp_ingr = False
exp_prep = False
cur_name = ''

def parseIngredients(line):
	ingredient = 'none'
	quantity = 'none'
	to_remove = ['(', ')']
	cleaned = line
	for inst in to_remove:
		cleaned = cleaned.replace(inst, '')
	if cleaned.count('.') == 0:
		quantity = re.search('([0-9]*[\/]*[0-9])', cleaned)
		if quantity == None:
			quantity = '1'
			ingredient = cleaned.strip()
		else:
			quantity = quantity.group(1)
			ingredient = cleaned.replace(quantity, '').strip()
		pass
	else:
		parsed = cleaned.split('.')
		quantity = parsed[0].strip()
		ingredient = parsed[1].strip()
	return (ingredient, quantity)
	
def parsePreparation(line):
	preparation = 'none'
	nutrition = 'none'
	parsed = line.split('Per Serving: ')
	preparation = parsed[0].strip()
	if len(parsed) > 1:
		nutrition = parsed[1].strip()
	return (preparation, nutrition)


def parseRecipe(line, line_index):
	global exp_name
	global exp_ingr
	global exp_prep
	global cur_name
	global recipe_df
	global ingr_df
	global recipe_ingr_df
	
	ignore = ['Could NOT Open Recipe Page Due To:', 'Conversion from type \'DBNull\' to type \'String\' is not valid.']

	if line in ignore:
		return 0
	
	if exp_name:
		print('name:', line)
		cur_name = line
		exp_name = False
	elif line == 'ingredients':
		exp_ingr = True
	elif line == 'preparation':
		exp_ingr = False
		exp_prep = True
	elif exp_ingr:
		parsed = parseIngredients(line)
		ingr_df.write(parsed[0]+'\n')
		recipe_ingr_df.write(str(line_index)+'<!><!><!>'+cur_name+'<!><!><!>'+parsed[0]+'<!><!><!>'+parsed[1]+'\n')
		print('ingr:', parsed)
	elif exp_prep:
		parsed = parsePreparation(line)
		print('prep:', parsed)
		recipe_df.write(str(line_index)+'<!><!><!>'+cur_name+'<!><!><!>'+parsed[0]+'<!><!><!>'+parsed[1]+'\n')
		return 1
	else:
		print('---UNRECOGNIZED INSTANCE---')
		print('Bad Instance: ', line)
	return 0
	
def main(input_file):
	global exp_name
	global exp_ingr
	global exp_prep
	global cur_name

	line_index = 0
	
	with open(input_file, 'r') as f:

		line = f.readline()
		while line != 'EOF':
		
			while line != '\n':
				nline = line.replace('\n', '')
				line_index += parseRecipe(nline, line_index)
				line = f.readline()
			exp_prep = False
			exp_name = True
			line = f.readline()

fnames = ['recipes']
recipe_df = open('recipe_df.txt', 'w')
ingr_df = open('ingr_df.txt', 'w')
recipe_ingr_df = open('recipe_ingr_df.txt', 'w')

for nm in fnames:

	input_file = nm+'.txt'
	main(input_file)

recipe_df.close()
ingr_df.close()
recipe_ingr_df.close()


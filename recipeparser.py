import re
import time

exp_name = True
exp_ingr = False
exp_prep = False

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


def parseRecipe(line):
	global exp_name
	global exp_ingr
	global exp_prep
	
	ignore = ['Could NOT Open Recipe Page Due To:', 'Conversion from type \'DBNull\' to type \'String\' is not valid.']
	
	if line in ignore:
		return
	
	if exp_name:
		print('name:', line)
		exp_name = False
	elif line == 'ingredients':
		exp_ingr = True
	elif line == 'preparation':
		exp_ingr = False
		exp_prep = True
	elif exp_ingr:
		print('ingr:', parseIngredients(line))
	elif exp_prep:
		print('prep:', line)
	else:
		print('---UNRECOGNIZED INSTANCE---')
	
def main(file_name):
	global exp_name
	global exp_ingr
	global exp_prep
	with open(file_name, 'r') as f:

		line = f.readline()
		while line != 'EOF':
		
			while line != '\n':
				nline = line.replace('\n', '')
				parseRecipe(nline)
				line = f.readline()
			exp_prep = False
			exp_name = True
			line = f.readline()

file_name = 'recipe_example.txt'
main(file_name)

#print('2 (8 oz.)  cans chopped clams, including juice'.replace('(', ''))

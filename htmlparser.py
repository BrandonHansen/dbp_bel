from html.parser import HTMLParser
import pandas as pd
# create a subclass and override the handler methods
#https://docs.python.org/2/library/htmlparser.html

def parsehtmlfile(in_file):

	out_file = 'recipes.txt'
	what_do_out = 'w'#write 'w' or append 'a', write writes over append just appends to bottom

	#open file for writing
	f = open(out_file, what_do_out)


	class MyHTMLParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			print("Encountered a start tag:", tag)

		def handle_endtag(self, tag):
			print("Encountered an end tag :", tag)

		def handle_data(self, data):
			print("Encountered some data  :", data)
			f.write(data+'\n')
	
	#open csv file in pandas, usecols only gets columns defined,
	#    add other column names like usecols=['category', 'title', 'info']
	df = pd.read_csv(in_file, usecols=['info'])

	#get particular column info by itself
	info = df['info']

	#loop through all and parse and put into file
	length = len(info)
	for index in range(0, length):
		parser = MyHTMLParser()
		parser.feed(info[index])
		f.write('\n')

	f.close()

ins = ['firstpage.csv']

for nm in ins:
	print(nm)
	parsehtmlfile('recipedata/'+nm)




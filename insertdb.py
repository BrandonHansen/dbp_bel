import MySQLdb

fs = ['recipe_df.txt']

bad_char = []

conn = MySQLdb.connect(host='localhost',
			user='bhansen4',
			passwd='pw',
			db="bhansen4")

x = conn.cursor()

for f in fs:
	with open(f, 'r') as fi:
		for line in fi:
			row = line
			for char in bad_char:
				row = row.replace(char, '')
			split_row = row.split('<!><!><!>');
			name = split_row[0]
			desc = split_row[1]
			nutr = split_row[2]
			try:
				x.execute("""INSERT INTO recipe VALUES (%s,%s,%s)""", (name, desc, nutr))
				conn.commit()
				print('insert '+name+' success')
			except:
				print('insert '+name+' fail')
				conn.rollback()

conn.close()

import MySQLdb
import time


fs = ['recipe_ingr_df.txt']

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
			ID = split_row[0]
			name = split_row[1]
			ingr = split_row[2]
			quant = split_row[3].strip()
			try:
				x.execute("""INSERT INTO recipe_ingr VALUES (%s,%s,%s,%s)""", (ID, name, ingr, quant))
				conn.commit()
				print('insert '+name+' success')
			except:
				print('insert '+name+' fail')
				conn.rollback()

conn.close()

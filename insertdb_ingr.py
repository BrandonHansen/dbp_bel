import MySQLdb
import time


fs = ['ingr_df.txt']

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
			ingr = split_row[1]
			try:
				x.execute("""INSERT INTO ingredient VALUES (%s, %s)""", (ID, ingr))
				conn.commit()
				print('insert '+name+' success')
			except:
				print('insert '+name+' fail')
				conn.rollback()

conn.close()

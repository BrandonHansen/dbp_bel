import MySQLdb
import time


fs = ['recipe_df.txt']

bad_char = []

conn = MySQLdb.connect(host='localhost',
			user='bhansen4',
			passwd='pw',
			db="bhansen4")

x = conn.cursor()

id_count = 0


x.execute("""SELECT COUNT(*) as cnt FROM recipe""")

for cnt in x:
	count = int(cnt[0])

for f in fs:
	with open(f, 'r') as fi:
		for line in fi:
			row = line
			for char in bad_char:
				row = row.replace(char, '')
			split_row = row.split('<!><!><!>');
			ID = split_row[0]
			name = split_row[1]
			desc = split_row[2]
			nutr = split_row[3].strip()
			try:
				x.execute("""INSERT INTO recipe_backup VALUES (%s,%s,%s,%s)""", (name, desc, nutr, ID))
				id_count = id_count + 1
				conn.commit()
				print('insert '+name+' success')
			except:
				print('insert '+name+' fail')
				conn.rollback()

conn.close()

import MySQLdb as mdb

con = mdb.connect('<insert>', '<insert>', '<insert>','<insert>')

with con:

#dictionary cursor
	cur = con.cursor(mdb.cursors.DictCursor)
	cur.execute('SELECT * FROM Writers')

	rows = cur.fetchall()

	for row in rows:
		print row['Id'], row['Name']

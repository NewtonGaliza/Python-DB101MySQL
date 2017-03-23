import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root','testdb')

with con:

	cur = con.cursor(mdb.cursors.DictCursor)
	cur.execute('SELECT * FROM Writers')

	rows = cur.fetchall()

	for row in rows:
		print row['Id'], row['Name']

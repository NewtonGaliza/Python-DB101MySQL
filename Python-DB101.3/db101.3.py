import MySQLdb as mdb

con = mdb.connect('<insert>', '<insert>', '<insert>', '<insert>')

with con:

#column headers
	cur = con.cursor()
	cur.execute('SELECT * FROM Writers')

	rows = cur.fetchall()

	desc = cur.description

	print ('%s %3s') % (desc[0][0], desc[1][0])

	for row in rows:
		print ('%2s %3s') % row

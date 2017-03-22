import MySQLdb as mdb

con = mdb.connect(host='<insert>', user='<insert>', passwd='<insert>', db='<insert>')

with con:

#create and populating a table
	cur = con.cursor()
	cur.execute('DROP TABLE IF EXISTS Writers')
	cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
	cur.execute("INSERT INTO Writers(Name) VALUES ('Stephen King')")
	cur.execute("INSERT INTO Writers(Name) VALUES ('Affonso Solano')")

	con.commit()

#retrieving data
	cur.execute('Select * FROM Writers')
	
	for i in range(cur.rowcount):
	    
	    row = cur.fetchone()
	    print row[0],row[1]

	'''
	rows = cur.fetchall()
	for row in rows:
		print (row)
	'''

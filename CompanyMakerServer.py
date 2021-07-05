def connect():
	create = not os.path.exists("Companies.sql")
	db = sqlite3.connect("Companies.sql")
	if create:
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE companies
			{id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL}""")

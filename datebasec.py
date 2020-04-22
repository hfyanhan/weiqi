def  cretet(cre):
	import sqlite3
	t=cre.cursor()
	#cre=sqlite3.connect("score2019.db")
	t.execute('''CREATE TABLE weiqi(
			 id text PRIMARY KEY,
			 name text,
			 place text,
			 time text,
			 black char(9),
			 white char(9),
			 result text,
			 tiehuan text,
			 fromb text,
			 fb text);''')
	cre.commit()
	#cre.close()


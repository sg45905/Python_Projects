'''
@author - Sarthak Gupta
'''

import sqlite3

# define database connection
class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('information.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists Comp(ID integer primary key autoincrement, Name varchar(255), Gender varchar(255), Comment text)')
		self._db.commit()
	
	# add into database
	def Add(self, name, gender, comment):
		self._db.execute('insert into Comp (Name, Gender, Comment) values (?,?,?)',(name,gender,comment))
		self._db.commit()
		
		return 'Your complaint has been submitted.'
	
	# list all complaints
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		
		return cursor

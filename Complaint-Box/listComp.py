from tkinter import *
from tkinter.ttk import *

from db import DBConnect

import sqlite3

# define class to list all complaints
class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		
		# define the root view
		self._root = Tk()
		self._root.title('List of Complaints')
		
		# define the table
		tv = Treeview(self._root)
		
		tv.pack()
		
		tv.heading('#0', text='ID')
		tv.configure(column=('#Name', '#Gender', '#Comment'))
		tv.heading('#Name', text='Name')
		tv.heading('#Gender', text='Gender')
		tv.heading('#Comment', text='Comment')
		
		cursor = self._dbconnect.ListRequest()
		
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
			tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])

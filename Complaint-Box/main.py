'''
@author - Sarthak Gupta
'''

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from db import DBConnect

from listComp import ListComp

# Config
conn = DBConnect()

root = Tk()
root.geometry('600x400')
root.title('Complaint Box')
root.configure(background='#104E8B')

# Style
style = Style()
style.theme_use('classic')

for elem in ['TLabel', 'TButton', 'TRadioutton']:
	style.configure(elem, background='#104E8B')

# Gridx1353
labels = ['Full Name:', 'Gender:', 'Comment:']

for i in range(3):
	Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

# list button
BuList = Button(root, text='List Comp.')
BuList.grid(row=4, column=1)

# submit button
BuSubmit = Button(root, text='Submit Now')
BuSubmit.grid(row=4, column=2)

# Entries
fullname = Entry(root, width=40, font=('Arial', 14))
fullname.grid(row=0, column=1, columnspan=2)

SpanGender = StringVar()
Radiobutton(root, text='Male', value='male', variable=SpanGender).grid(row=1, column=1)
Radiobutton(root, text='Female', value='female', variable=SpanGender).grid(row=1, column=2)

comment = Text(root, width=35, height=5, font=('Arial', 14))
comment.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# save data
def SaveData():
	msg = conn.Add(fullname.get(), SpanGender.get(), comment.get(1.0, 'end'))
	fullname.delete(0, 'end')
	comment.delete(1.0, 'end')
	showinfo(title='Add Info', message=msg)

# show list
def ShowList():
	listrequest = ListComp()

BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

root.mainloop()

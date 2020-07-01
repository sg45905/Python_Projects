'''
@author - Sarthak Gupta
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# define frame and all
root = Tk()
frame_header = ttk.Frame(root)
frame_header.pack()

headerlabel = ttk.Label(frame_header, text='CUSTOMER FEEDBACK SYSTEM', foreground='Green', font=('Arial', 24))
headerlabel.grid(row=0, column=1)

messagelabel = ttk.Label(frame_header, text='YOUR FEEDBACK IS WAY TOO VALUABLE FOR US...', foreground='blue', font=('Arial', 10))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()

name = StringVar()
email = StringVar()

# entries
namelabel = ttk.Label(frame_content, text='Name')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=name)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(frame_content, text='Email')
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=email)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)
textcomment.config(wrap ='word')

# clear function
def clear():
    global entry_name
    global entry_email
    global textcomment
    
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)

# submit function
def submit():
    global entry_name
    global entry_email
    global textcomment
    
    print(f'Name: {name.get()}')
    print(f'Email: {email.get()}')
    print(f'Comment: {textcomment.get(1.0, END)}')
    
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback')
    
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)

# buttons
submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')

# main loop to run the program
mainloop()

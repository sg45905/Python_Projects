from tkinter import *
from tkinter import messagebox

import os

f = open("database_proj", 'a+')

# define and configure the root window
root = Tk()
root.title("Pharmacy Managment System")
root.configure(width=1500, height=600, bg='BLACK')
var = -1

# define the add item method
def addItem():
    global var

    num_lines = 0
    
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    
    var = num_lines-1

    name1 = name.get()
    price1 = price.get()
    qty1 = qty.get()
    cat1 = cat.get()
    disc1 = disc.get()
    
    f.write(f'{str(name1)} {price1} {qty1} {str(cat1)} {disc1}\n')
    
    name.delete(0, END)
    price.delete(0, END)
    qty.delete(0, END)
    cat.delete(0, END)
    disc.delete(0, END)

# define the view first item method
def firstItem():
    global var
    
    var=0
    
    f.seek(var)
    
    c=f.readline()
    
    v=list(c.split(" "))
    
    name.delete(0, END)
    price.delete(0, END)
    qty.delete(0, END)
    cat.delete(0, END)
    disc.delete(0, END)
    
    name.insert(0, str(v[0]))
    price.insert(0, str(v[1]))
    qty.insert(0, str(v[2]))
    cat.insert(0, str(v[3]))
    disc.insert(0, str(v[4]))

# define the view next item method
def nextItem():
    global var
    
    var = var + 1
    
    f.seek(var)
    
    try:
        c=f.readlines()
        
        xyz = c[var]
        
        v = list(xyz.split(" "))
        
        name.delete(0, END)
        price.delete(0, END)
        qty.delete(0, END)
        cat.delete(0, END)
        disc.delete(0, END)
        
        name.insert(0, str(v[0]))
        price.insert(0, str(v[1]))
        qty.insert(0, str(v[2]))
        cat.insert(0, str(v[3]))
        disc.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

# define the view previous item method
def previousItem():
        global var

        var=var-1
        
        f.seek(var)
        
        try:
            z = f.readlines()
            
            xyz=z[var]
            
            v = list(xyz.split(" "))
            
            name.delete(0, END)
            price.delete(0, END)
            qty.delete(0, END)
            cat.delete(0, END)
            disc.delete(0, END)

            name.insert(0, str(v[0]))
            price.insert(0, str(v[1]))
            qty.insert(0, str(v[2]))
            cat.insert(0, str(v[3]))
            disc.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

# define the view last item method
def lastItem():
    global var

    f4=open("database_proj",'r')
    
    x=f4.read().splitlines()
    
    last_line= x[-1]
    num_lines = 0
    
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    
    var=num_lines-1

    try:
        v = list(last_line.split(" "))
        
        name.delete(0, END)
        price.delete(0, END)
        qty.delete(0, END)
        cat.delete(0, END)
        disc.delete(0, END)

        name.insert(0, str(v[0]))
        price.insert(0, str(v[1]))
        qty.insert(0, str(v[2]))
        cat.insert(0, str(v[3]))
        disc.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

# define the search item method
def searchItem():
    i=0
    
    name1 = name.get()
    
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            
            if str(name1) in line:
                break
        
        try:
            v = list(line.split(" "))
            
            name.delete(0, END)
            price.delete(0, END)
            qty.delete(0, END)
            cat.delete(0, END)
            disc.delete(0, END)
            
            name.insert(0, str(v[0]))
            price.insert(0, str(v[1]))
            qty.insert(0, str(v[2]))
            cat.insert(0, str(v[3]))
            disc.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "error end of file")
    
    working.close()

# deifne the clear all method
def clearItem():
    name.delete(0, END)
    price.delete(0, END)
    qty.delete(0, END)
    cat.delete(0, END)
    disc.delete(0, END)

# define the labels and the entry fields
label0 = Label(root, text="PHARMACY MANAGEMENT SYSTEM ", bg="black", fg="white", font=("Times", 30))

label1 = Label(root, text="Enter Item Name", bg="Blue", relief="ridge", fg="white", font=("Times", 12), width=25)
name = Entry(root, font=("Times", 12))

label2 = Label(root, text="Enter price", bd="2", relief="ridge", height="1", bg="blue", fg="white", font=("Times", 12), width=25)
price = Entry(root, font=("Times", 12))

label3 = Label(root, text="Enter Quantity", bd="2", relief="ridge", bg="Blue", fg="white", font=("Times", 12), width=25)
qty = Entry(root, font=("Times", 12))

label4 = Label(root, text="Enter category", bd="2", relief="ridge", bg="blue", fg="white", font=("Times", 12), width=25)
cat = Entry(root, font=("Times", 12))

label5 = Label(root, text="Enter discount", bg="blue", relief="ridge", fg="white", font=("Times", 12), width=25)
disc = Entry(root, font=("Times", 12))

# define buttons
button1 = Button(root, text="Add item", bg="white", fg="black", width=20, font=("Times", 12), command=addItem)
button2 = Button(root, text="View item on top", bg="white", fg="black", width =20, font=("Times", 12), command=firstItem)
button3 = Button(root, text="View item at end", bg="white", fg="black", width =20, font=("Times", 12), command=lastItem)
button4 = Button(root, text="View next item" , bg="white", fg="black", width =20, font=("Times", 12), command=nextItem)
button5 = Button(root, text="View previous item", bg="white", fg="black", width =20, font=("Times", 12), command=previousItem)
button6 = Button(root, text="Search some item", bg="white", fg="black", width =20, font=("Times", 12), command=searchItem)
button7= Button(root, text="Clear screen", bg="white", fg="black", width=20, font=("Times", 12), command=clearItem)

# place everything on the grid
label0.grid(columnspan=6, padx=10, pady=10)

label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)

name.grid(row=1, column=1, padx=40, pady=10)
price.grid(row=2, column=1, padx=10, pady=10)
qty.grid(row=3, column=1, padx=10, pady=10)
cat.grid(row=4, column=1, padx=10, pady=10)
disc.grid(row=5, column=1, padx=10, pady=10)

button1.grid(row=1, column=4, padx=40, pady=10)
button2.grid(row=1, column=5, padx=40, pady=10)
button3.grid(row=2, column=4, padx=40, pady=10)
button4.grid(row=2, column=5, padx=40, pady=10)
button5.grid(row=3, column=4, padx=40, pady=10)
button6.grid(row=3, column=5, padx=40, pady=10)
button7.grid(row=4, column=4, padx=40, pady=10)

# main program loop
root.mainloop()

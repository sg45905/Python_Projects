from tkinter import *
from tkinter import messagebox as ms
from datetime import datetime

import math
import sqlite3

with sqlite3.connect('E:/Documents/Programs/Python/Equation-Solver/cred.db') as db:
    c1 = db.cursor()

c1.execute('CREATE TABLE IF NOT EXISTS eq (tp TEXT NOT NULL, frml TEXT NOT NULL, dt TEXT NOT NULL)')

db.commit()

class Intro:
    def __init__(self, master):
        self.master = master
        self.master.title('Sarthak Gupta | Equation Solver')
        self.master.geometry('500x200')
        self.master.configure(bg='black')
        self.introWidget()
    
    def introo(self):
        self.newWindow = Toplevel(self.master)
        self.app = Tpeq(self.newWindow)
    
    def introWidget(self):
        self.root = root

        self.head = Label(self.master, relief='ridge', width=41, text="Welcome to this Advanced Equation Solver", font=('Times', 15, 'bold'), pady=10, bg='blue')
        self.head.place(x=0, y=0)

        self.button1 = Button(root, text="Click here to continue", width=16, font=('Times', 25, 'bold'), bd=6, bg='#FF0000', command=self.introo)
        self.button1.place(x=80, y=100)
        
        self.root.mainloop()

class Tpeq:
    def __init__(self, master):
        self.master = master
        self.master.title('Equation Solver | Equation Type')
        self.master.configure(bg='black')
        self.tpeqWidget()
    
    def lb1(self):
        self.newWindow = Toplevel(self.master)
        self.app = TmFlt(self.newWindow)
    
    def lb2(self):
        self.newWindow = Toplevel(self.master)
        self.app = RngPrbl(self.newWindow)
    
    def lb3(self):
        self.newWindow = Toplevel(self.master)
        self.app = HgtPrbl(self.newWindow)
    
    def lb4(self):
        self.newWindow = Toplevel(self.master)
        self.app = TrjctrPrjctl(self.newWindow)
    
    def hstr(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hstr(self.newWindow)
    
    def ext(self):
        ms.showinfo('Jaa rahe ho, tussi na jao', 'Thanks for using this system')
        root.destroy()

    def tpeqWidget(self):
        self.lbl = Label(self.master, text='Choose your equation', relief='ridge', bg='yellow', font=('Times', 15, 'bold'), width=20)

        self.lbl1 = Label(self.master, text='Time of flight', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=17)
        self.btn1 = Button(self.master, text='Click here', relief='ridge', bg='green', font=('Times', 15, 'bold'), command=self.lb1)

        self.lbl2 = Label(self.master, text='Range of Projection', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=17)
        self.btn2 = Button(self.master, text='Click here', relief='ridge', bg='green', font=('Times', 15, 'bold'), command=self.lb2)

        self.lbl3 = Label(self.master, text='Height of Projection', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=17)
        self.btn3 = Button(self.master, text='Click here', relief='ridge', bg='green', font=('Times', 15, 'bold'), command=self.lb3)

        self.lbl4 = Label(self.master, text='Trajectory of Projectile', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=17)
        self.btn4 = Button(self.master, text='Click here', relief='ridge', bg='green', font=('Times', 15, 'bold'), command=self.lb4)

        self.btn = Button(self.master, text='History Check', relief='ridge', bg='red', font=('Times', 15, 'bold'), command=self.hstr)
        self.extbtn = Button(self.master, text='Exit', relief='ridge', bg='red', font=('Times', 15, 'bold'), command=self.ext)

        self.lbl.grid(columnspan=2, padx=10)

        self.lbl1.grid(row=1, column=0, pady=10)
        self.btn1.grid(row=1, column=1, pady=10)

        self.lbl2.grid(row=2, column=0, pady=10, padx=10)
        self.btn2.grid(row=2, column=1, pady=10, padx=10)

        self.lbl3.grid(row=3, column=0, pady=10)
        self.btn3.grid(row=3, column=1, pady=10)

        self.lbl4.grid(row=4, column=0, pady=10, padx=10)
        self.btn4.grid(row=4, column=1, pady=10, padx=10)

        self.btn.grid(row=5, column=0)
        self.extbtn.grid(row=5, column=1)

class TmFlt:
    def __init__(self, master):
        self.master = master
        self.master.title('Equation Solver | Time of Flight')
        self.master.configure(bg='black')
        self.tmfltWidget()
    
    def calc(self):
        self.now = datetime.now().strftime('%B %d, %Y - %H:%M:%S')

        self.u1 = int(self.u.get())
        self.tht1 = self.tht.get().split()

        for i in range(len(self.tht1)):
            thtl = int(self.tht1[i])
            t = int((2 * self.u1 * math.sin(thtl * (math.pi/180))) / 9.8)
            self.tf.set(str(t))

            self.l1 = Label(self.master, text=i+1, relief='ridge', bg='green', font=('Times', 15, 'bold'), width=10)
            self.l2 = Label(self.master, text=self.u.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l3 = Label(self.master, text=str(thtl), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l4 = Label(self.master, text=self.tf.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)

            self.l1.grid(row=5+i, column=0)
            self.l2.grid(row=5+i, column=1)
            self.l3.grid(row=5+i, column=2)
            self.l4.grid(row=5+i, column=3)
        
        with sqlite3.connect('E:/Documents/Programs/Python/Equation-Solver/cred.db') as db:
            c2 = db.cursor()
        
        msg = 'INSERT INTO eq (tp, frml, dt) values (?, ?, ?)'
        c2.execute(msg, [('Time of Flight'), ('(2u sin(θ)) / g'), (self.now)])

        db.commit()
    
    def bck(self):
        self.master.destroy()
    
    def tmfltWidget(self):
        self.u = StringVar()
        self.tht = StringVar()
        self.tf = StringVar()

        self.u.set('0')
        self.tht.set('0')
        self.tf.set('')

        self.lbl = Label(self.master, text='Calculate the Time of Flight', relief='ridge', bg='yellow', font=('Times', 15, 'bold'), width=25)
        
        self.lbl1 = Label(self.master, text='Enter the Initial Velocity, u (in m/s)          :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e1 = Entry(self.master, textvariable=self.u, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.lbl2 = Label(self.master, text='Enter Angle of Projection, θ (in degrees) :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e2 = Entry(self.master, textvariable=self.tht, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.btn = Button(self.master, text='Calculate', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.calc)
        self.bckbtn = Button(self.master, text='Back', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.bck)

        self.snlbl = Label(self.master, text='Serial No.', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=10)
        self.ivlbl = Label(self.master, text='Initial Velocity (u)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.aplbl = Label(self.master, text='Angle of Projection (θ)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.tflbl = Label(self.master, text='Time of Flight (in sec.)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)

        self.lbl.grid(column=1, columnspan=2, padx=10)

        self.lbl1.grid(row=1, column=1, pady=10)
        self.e1.grid(row=1, column=2, pady=10)

        self.lbl2.grid(row=2, column=1, padx=10, pady=10)
        self.e2.grid(row=2, column=2, padx=10, pady=10)

        self.btn.grid(row=3, column=1)
        self.bckbtn.grid(row=3, column=2)

        self.snlbl.grid(row=4, column=0, padx=10, pady=10)
        self.ivlbl.grid(row=4, column=1, padx=10, pady=10)
        self.aplbl.grid(row=4, column=2, padx=10, pady=10)
        self.tflbl.grid(row=4, column=3, padx=10, pady=10)

class RngPrbl:
    def __init__(self, master):
        self.master = master
        self.master.title('Equation Solver | Range of Projection')
        self.master.configure(bg='black')
        self.rngprblWidget()
    
    def calc(self):
        self.now = datetime.now().strftime('%B %d, %Y - %H:%M:%S')

        self.u1 = int(self.u.get())
        self.tht1 = self.tht.get().split()

        for i in range(len(self.tht1)):
            thtl = int(self.tht1[i])
            r = int((math.pow(self.u1, 2) * math.sin(2*(thtl*(math.pi/180)))) / 9.8)
            self.rp.set(str(r))

            self.l1 = Label(self.master, text=i+1, relief='ridge', bg='green', font=('Times', 15, 'bold'), width=10)
            self.l2 = Label(self.master, text=self.u.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l3 = Label(self.master, text=str(thtl), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l4 = Label(self.master, text=self.rp.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)

            self.l1.grid(row=5+i, column=0)
            self.l2.grid(row=5+i, column=1)
            self.l3.grid(row=5+i, column=2)
            self.l4.grid(row=5+i, column=3)
        
        with sqlite3.connect('E:/Documents/Programs/Python/Equation-Solver/cred.db') as db:
            c = db.cursor()
        
        msg = 'INSERT INTO eq (tp, frml, dt) values (?, ?, ?)'
        c.execute(msg, [('Range of Projection'), ('(u*u sin(2θ)) / g'), (self.now)])
        
        db.commit()
    
    def bck(self):
        self.master.destroy()
    
    def rngprblWidget(self):
        self.u = StringVar()
        self.tht = StringVar()
        self.rp = StringVar()

        self.u.set('0')
        self.tht.set('0')
        self.rp.set('')

        self.lbl = Label(self.master, text='Calculate Range of Projection', relief='ridge', bg='yellow', font=('Times', 15, 'bold'), width=25)
        
        self.lbl1 = Label(self.master, text='Enter the Initial Velocity, u (in m/s)          :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e1 = Entry(self.master, textvariable=self.u, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.lbl2 = Label(self.master, text='Enter Angle of Projection, θ (in degrees) :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e2 = Entry(self.master, textvariable=self.tht, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.btn = Button(self.master, text='Calculate', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.calc)
        self.bckbtn = Button(self.master, text='Back', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.bck)

        self.snlbl = Label(self.master, text='Serial No.', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=10)
        self.ivlbl = Label(self.master, text='Initial Velocity (u)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.aplbl = Label(self.master, text='Angle of Projection (θ)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.rplbl = Label(self.master, text='Range of Projection (in mtr.)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)

        self.lbl.grid(column=1, columnspan=2, padx=10)

        self.lbl1.grid(row=1, column=1, pady=10)
        self.e1.grid(row=1, column=2, pady=10)

        self.lbl2.grid(row=2, column=1, padx=10, pady=10)
        self.e2.grid(row=2, column=2, padx=10, pady=10)

        self.btn.grid(row=3, column=1)
        self.bckbtn.grid(row=3, column=2)

        self.snlbl.grid(row=4, column=0, padx=10, pady=10)
        self.ivlbl.grid(row=4, column=1, padx=10, pady=10)
        self.aplbl.grid(row=4, column=2, padx=10, pady=10)
        self.rplbl.grid(row=4, column=3, padx=10, pady=10)

class HgtPrbl:
    def __init__(self, master):
        self.master = master
        self.master.title('Equation Solver | Height of Projection')
        self.master.configure(bg='black')
        self.hgtprblWidget()
    
    def calc(self):
        self.now = datetime.now().strftime('%B %d, %Y - %H:%M:%S')

        self.u1 = int(self.u.get())
        self.tht1 = self.tht.get().split()

        for i in range(len(self.tht1)):
            thtl = int(self.tht1[i])
            h = int(math.pow((self.u1 * math.sin(thtl*(math.pi/180))), 2) / (2*9.8))
            self.hp.set(str(h))

            self.l1 = Label(self.master, text=i+1, relief='ridge', bg='green', font=('Times', 15, 'bold'), width=10)
            self.l2 = Label(self.master, text=self.u.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l3 = Label(self.master, text=str(thtl), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l4 = Label(self.master, text=self.hp.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)

            self.l1.grid(row=5+i, column=0)
            self.l2.grid(row=5+i, column=1)
            self.l3.grid(row=5+i, column=2)
            self.l4.grid(row=5+i, column=3)
        
        with sqlite3.connect('E:/Documents/Programs/Python/Equation-Solver/cred.db') as db:
            c = db.cursor()
        
        msg = 'INSERT INTO eq (tp, frml, dt) values (?, ?, ?)'
        c.execute(msg, [('Height of Projection'), ('(u sin(θ)*(u sin(θ))) / 2*g'), (self.now)])
        
        db.commit()
    
    def bck(self):
        self.master.destroy()
    
    def hgtprblWidget(self):
        self.u = StringVar()
        self.tht = StringVar()
        self.hp = StringVar()

        self.u.set('0')
        self.tht.set('0')
        self.hp.set('')

        self.lbl = Label(self.master, text='Calculate Height of Projection', relief='ridge', bg='yellow', font=('Times', 15, 'bold'), width=25)
        
        self.lbl1 = Label(self.master, text='Enter the Initial Velocity, u (in m/s)          :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e1 = Entry(self.master, textvariable=self.u, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.lbl2 = Label(self.master, text='Enter Angle of Projection, θ (in degrees) :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e2 = Entry(self.master, textvariable=self.tht, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.btn = Button(self.master, text='Calculate', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.calc)
        self.bckbtn = Button(self.master, text='Back', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.bck)

        self.snlbl = Label(self.master, text='Serial No.', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=10)
        self.ivlbl = Label(self.master, text='Initial Velocity (u)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.aplbl = Label(self.master, text='Angle of Projection (θ)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.hplbl = Label(self.master, text='Height of Projection (in mtr.)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)

        self.lbl.grid(column=1, columnspan=2, padx=10)

        self.lbl1.grid(row=1, column=1, pady=10)
        self.e1.grid(row=1, column=2, pady=10)

        self.lbl2.grid(row=2, column=1, padx=10, pady=10)
        self.e2.grid(row=2, column=2, padx=10, pady=10)

        self.btn.grid(row=3, column=1)
        self.bckbtn.grid(row=3, column=2)

        self.snlbl.grid(row=4, column=0, padx=10, pady=10)
        self.ivlbl.grid(row=4, column=1, padx=10, pady=10)
        self.aplbl.grid(row=4, column=2, padx=10, pady=10)
        self.hplbl.grid(row=4, column=3, padx=10, pady=10)

class TrjctrPrjctl:
    def __init__(self, master):
        self.master = master
        self.master.title('Equation Solver | Trajectory of Projectile')
        self.master.configure(bg='black')
        self.trjctprjctlWidget()
    
    def calc(self):
        self.now = datetime.now().strftime('%B %d, %Y - %H:%M:%S')

        self.u1 = int(self.u.get())
        self.tht1 = self.tht.get().split()

        for i in range(len(self.tht1)):
            thtl = int(self.tht1[i])
            t = int((2 * self.u1 * math.sin(thtl * (math.pi/180))) / 9.8)
            r = int((math.pow(self.u1, 2) * math.sin(2*(thtl*(math.pi/180)))) / 9.8)
            h = int(math.pow((self.u1 * math.sin(thtl*(math.pi/180))), 2) / (2*9.8))
            self.tf.set(str(t))
            self.rp.set(str(r))
            self.hp.set(str(h))

            self.l1 = Label(self.master, text=self.u.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l2 = Label(self.master, text=str(thtl), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l3 = Label(self.master, text=self.tf.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l4 = Label(self.master, text=self.rp.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l5 = Label(self.master, text=self.hp.get(), relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)

            self.l1.grid(row=5+i, column=0)
            self.l2.grid(row=5+i, column=1)
            self.l3.grid(row=5+i, column=2)
            self.l4.grid(row=5+i, column=3)
            self.l5.grid(row=5+i, column=4)
        
        # with sqlite3.connect('E:/Documents/Programs/Python/Equation-Solver/cred.db') as db:
        #     c = db.cursor()
        
        # msg = 'INSERT INTO eq (tp, frml, dt) values (?, ?, ?)'
        # c.execute(msg, [('Height of Projection'), ('(u sin(θ)*(u sin(θ))) / 2*g'), (self.now)])
        
        # db.commit()
    
    def bck(self):
        self.master.destroy()
    
    def trjctprjctlWidget(self):
        self.u = StringVar()
        self.tht = StringVar()
        self.tf = StringVar()
        self.rp = StringVar()
        self.hp = StringVar()

        self.u.set('0')
        self.tht.set('0')
        self.tf.set('')
        self.rp.set('')
        self.hp.set('')

        self.lbl = Label(self.master, text='Trajectory of Projectile', relief='ridge', bg='yellow', font=('Times', 15, 'bold'), width=20)
        
        self.lbl1 = Label(self.master, text='Enter the Initial Velocity, u (in m/s)          :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e1 = Entry(self.master, textvariable=self.u, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.lbl2 = Label(self.master, text='Enter Angle of Projection, θ (in degrees) :', relief='ridge', bg='blue', font=('Times', 15, 'bold'), width=30)
        self.e2 = Entry(self.master, textvariable=self.tht, relief='ridge', bg='white', font=('Times', 15, 'bold'), width=30)

        self.btn = Button(self.master, text='Display Graph', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.calc)
        self.bckbtn = Button(self.master, text='Back', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.bck)

        self.ivlbl = Label(self.master, text='Initial Velocity (u)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.aplbl = Label(self.master, text='Angle of Projection (θ)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.tflbl = Label(self.master, text='Time of Flight (in sec.)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.rplbl = Label(self.master, text='Range of Projection (in mtr.)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        self.hplbl = Label(self.master, text='Height of Projection (in mtr.)', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=20)
        
        self.lbl.grid(column=1, columnspan=2, padx=10)

        self.lbl1.grid(row=1, column=1, pady=10)
        self.e1.grid(row=1, column=2, pady=10)

        self.lbl2.grid(row=2, column=1, padx=10, pady=10)
        self.e2.grid(row=2, column=2, padx=10, pady=10)

        self.btn.grid(row=3, column=1)
        self.bckbtn.grid(row=3, column=2)

        self.ivlbl.grid(row=4, column=0, padx=10, pady=10)
        self.aplbl.grid(row=4, column=1, padx=10, pady=10)
        self.tflbl.grid(row=4, column=2, padx=10, pady=10)
        self.rplbl.grid(row=4, column=3, padx=10, pady=10)
        self.hplbl.grid(row=4, column=4, padx=10, pady=10)

class Hstr:
    def __init__(self, master):
        self.master = master
        self.master.title('Equation Solver | History')
        self.master.configure(bg='black')
        self.hstrWidget()
    
    def bck(self):
        self.master.destroy()
    
    def hstrWidget(self):
        self.lbl = Label(self.master, text='History', relief='ridge', bg='yellow', font=('Times', 15, 'bold'), width=20)

        self.tplbl = Label(self.master, text='Type of the equation', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=30)
        self.frmllbl = Label(self.master, text='Formula of the equation', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=30)
        self.dtlbl = Label(self.master, text='Date and Time of the calculation', relief='ridge', bg='orange', font=('Times', 15, 'bold'), width=30)
        self.extbtn = Button(self.master, text='Back', relief='ridge', bg='red', font=('Times', 15, 'bold'), width=10, command=self.bck)

        self.lbl.grid(column=1, padx=10)

        self.tplbl.grid(row=1, column=0, pady=10)
        self.frmllbl.grid(row=1, column=1, pady=10)
        self.dtlbl.grid(row=1, column=2, pady=10)

        self.extbtn.grid(row=13, column=1, padx=10)

        with sqlite3.connect('E:/Documents/Programs/Python/Equation-Solver/cred.db') as db:
            c3 = db.cursor()
        
        msg = 'SELECT * FROM (SELECT * FROM eq ORDER BY dt DESC LIMIT 10)Var1 ORDER BY dt ASC'
        c3.execute(msg)
        rslt = c3.fetchall()

        for i in range(len(rslt)):
            self.l1 = Label(self.master, text=rslt[i][0], relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l2 = Label(self.master, text=rslt[i][1], relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)
            self.l3 = Label(self.master, text=rslt[i][2], relief='ridge', bg='green', font=('Times', 15, 'bold'), width=20)

            self.l1.grid(row=2+i, column=0, pady=10)
            self.l2.grid(row=2+i, column=1, pady=10)
            self.l3.grid(row=2+i, column=2, pady=10)

if __name__ == '__main__':
    root = Tk()
    Intro(root)
    root.mainloop()

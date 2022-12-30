from tkinter import *
from tkinter import ttk 
import mysql.connector
from mysql.connector import Error
from tkinter import *
from PIL import Image, ImageTk
from time import sleep

def run(stats):
    b_fg=stats[0]; b_bg=stats[1]
    background=stats[2]
    f=list(stats[3])
    f[1]=18
    f=tuple(f)
    entry_bg=stats[4]; label_fg=stats[5]
    entry_select_bg=stats[6]
    global sql_u,sql_p
    sql_u=stats[7]; sql_p=stats[8]

    w = Tk()
    w.title("EmployeeDBManagement: View All Records In Database")
    w.configure(bg=background); w.state('zoomed')
    w.iconbitmap('emp_detailsall.ico')
    global table,scroll_bar

    w.focus_force()
    frame=Frame(w,bg='black')
    frame.pack(padx=10,pady=10,fill=BOTH)
    ttk.Style().configure("Treeview",font=('Comic Sans MS', 11)) # Modify the font of the body
    ttk.Style().configure("Treeview.Heading", font=('Comic Sans MS', 13,'bold')) # Modify the font of the headings
    ttk.Style().layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    table=ttk.Treeview(frame,height = 28)
    columns=['EMPLOYEE ID','NAME','DOB','ADDRESS','BANK ACCOUNT NUMBER','PAN CARD NUMBER',
             'DESIGNATION','DEPARTMENT','REPORTING MANAGER','EARNED LEAVE',
             'PAID LEAVE','SALARY','NET PAY','INCOME TAX','BONUS']
    
    table['style']='Treeview'

    b1=Button(w,text='Exit',background=b_bg,relief='solid',font=f,
                 activebackground=b_bg,bd=3,foreground=b_fg,
                 highlightbackground='blue',command=w.destroy)

    xscroll_bar=ttk.Scrollbar(frame,orient='horizontal',command=table.xview)
    yscroll_bar=ttk.Scrollbar(frame,orient='vertical',command=table.yview)

    table.configure(xscrollcommand=xscroll_bar.set)
    table.configure(yscrollcommand=yscroll_bar.set)

    xscroll_bar.pack(side=BOTTOM,fill=X)
    yscroll_bar.pack(side=RIGHT,fill=Y)

    b1.focus()
    b1.bind('<Return>',lambda e:b1.invoke())
    def display(records):
        table['columns']=columns
        for i in columns:
            table.heading(i,text=i)
            table.column(i,stretch=YES,anchor='center',minwidth=150)
        table.column('#0',width=1,stretch=NO)
        '''To remove the default column which is of no use to us
        since we can not put any values in this column'''
        for i in records: table.insert('','end',values=i)
        table.pack(expand=True,fill=BOTH,padx=5,pady=5)
        b1.pack(padx=5,pady=5,expand=True,fill=BOTH)
                
    def connect():
        global db,cursor; db = None
        try:
            db = mysql.connector.connect(host = "localhost", database = 'edms',
            user = sql_u, password = sql_p)
            cursor = db.cursor()
            query = "select * from employee;"
            cursor.execute(query)
            rec = cursor.fetchall()
            display(rec)            
            cursor.close()
        except Error as e: print(e)
        finally:
            if db is not None and db.is_connected(): db.close()
                #print(db)
                #print(db.is_connected())
    connect()
    mainloop()    

from tkinter import *
from tkinter import ttk 
import mysql.connector
from mysql.connector import Error
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
    sql_u=stats[7]; sql_p=stats[8]
    
    w = Tk(); w.configure(bg = 'black')
    w.title("EmployeeDBManagement: Employees Details (Designation-based)")
    w.focus_force(); w.resizable(False,False)
    w.iconbitmap('emp_designationbased.ico')
    def error():
        w.attributes('-topmost',True)
        messagebox.showerror("Error","Invalid Designation")
        w.attributes('-topmost',False)
        w.focus_force()

    def display():
        global cursor,db,count
        cond = str(drop.get())
        if cond != "Select Designation":
            query = "select * from employee where designation ='{0}'".format(cond)
            cursor.execute(query)
            rec = cursor.fetchall()
            for selected_item in table.get_children():
                table.delete(selected_item)
            if count==0:
                w.geometry('500x350')
                w.minsize(500,350)
                xscroll_bar.pack(side=BOTTOM,fill=X)
                yscroll_bar.pack(side=RIGHT,fill=Y)
                '''setting up the columns'''
                columns=['EMPLOYEE ID','NAME','DOB','ADDRESS','BANK ACCOUNT NUMBER','PAN CARD NUMBER',
             'DESIGNATION','DEPARTMENT','REPORTING MANAGER','EARNED LEAVE',
             'PAID LEAVE','SALARY','NET PAY','INCOME TAX','BONUS']
                table['columns']=columns
                for i in columns:
                    table.heading(i,text=i)
                    table.column(i,stretch=YES,anchor='center',minwidth=120)
                table.column('#0',width=1,stretch=NO)
            for i in rec:
                table.insert('','end',values=i)
            count+=1
            table.pack(expand=True,fill=BOTH,pady=5,padx=5)
            w.resizable(True,True)
        else:
            error()
    global frame1,frame2,cursor,db,count
    db = mysql.connector.connect(host = "localhost", database = 'edms',user = sql_u,password = sql_p)
    cursor = db.cursor()
    count=0
    
    fr=Frame(w,bg=background)
    fr.pack(padx=5,pady=5,expand=True,fill=BOTH)
    frame1=Frame(fr,bg=background)
    frame1.pack(padx=10,pady=10,fill=BOTH,expand=True)
    frame2=Frame(fr,bg=background,width=10,height=10)
    frame2.pack(padx=10,pady=10,fill=BOTH,expand=True)

    table=ttk.Treeview(frame1)
    xscroll_bar=ttk.Scrollbar(frame1,orient='horizontal',command=table.xview)
    yscroll_bar=ttk.Scrollbar(frame1,orient='vertical',command=table.yview)

    table.configure(xscrollcommand=xscroll_bar.set)
    table.configure(yscrollcommand=yscroll_bar.set)

        
    """ Connect to MySQL database """
    query2 = "select distinct designation from employee;" 
    cursor.execute(query2) 
    desigs = cursor.fetchall()
    desigs1 = [i[0] for i in desigs] 
    drop = ttk.Combobox(frame2)
    
    drop.pack(fill=BOTH,side=LEFT,pady=5,expand=True)
    drop.set("Select Designation")
    drop['values']=desigs1

    del_b = Button(frame2,bd=3,text='Reshow the table',
             background=b_bg,relief='solid',font=f,
             activebackground=b_bg,wraplength=290,
             highlightbackground='blue',command = display)
    del_b.pack(fill=BOTH,padx=10,pady=5,expand=True)
    del_b.focus()
    del_b.bind('<Left>',lambda e:drop.focus_set())
    del_b.bind('<Return>',lambda e:del_b.invoke())

    drop.bind('<Right>',lambda e:del_b.focus_set())
    mainloop()

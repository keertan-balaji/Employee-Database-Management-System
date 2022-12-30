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
    global l1,e,l2,sql_u,sql_p
    l2=0
    sql_u=stats[7]; sql_p=stats[8]
   
    
    def error():
        messagebox.showerror("Error","Invalid Employee ID")
        w.attributes('-topmost',True)
        w.focus_force()
        w.attributes('-topmost',False)
        e.focus()

    def sql():
        try:
            db=mysql.connector.connect(host='localhost',database='edms',user=sql_u,password=sql_p)
            cursor=db.cursor()
            i=e.get()
            cursor.execute('select salary,netpay,itax,bonus from employee where emp_id={0};'.format(i))
            rec=cursor.fetchall()
            if rec!=[]:    
                top=Toplevel()
                top.title('Details')
                top.configure(background='black')
                top.iconbitmap('emp_salarydetails.ico')

                fr=Frame(top,bg=background)
                fr.pack(padx=5,pady=5)
                labels1 = labels2 = []
                text=['Salary:','Netpay:','Income Tax:','Bonus:']
                for i in range(4):
                    label1=Label(fr,text=text[i],font = f, fg = label_fg,bg = background)
                    label2=Label(fr,text=str(rec[0][i]),font = f, fg = label_fg,bg = background)
                    label1.grid(row=i,padx=10,pady=10)
                    label2.grid(row=i,column=1,padx=10,pady=10)
                    labels1.append(label1)
                    labels2.append(label2)
            else: error()
        except: error()

    w=Tk()
    w.configure(bg='black')
    w.title('EmployeeDBManagement: One Employee\'s Salary Details')
    w.iconbitmap('emp_salarydetails.ico')
    w.focus_force()
    frame=Frame(w,bg=background)
    frame.pack(pady=5,padx=5)

    l1=Label(frame,text='Enter Employee ID:',font = f, fg = label_fg,bg = background)
    l2=Label(frame,wraplength=200,font = f,fg = label_fg,bg = background)

    e=Entry(frame,bg = entry_bg,font = f,selectbackground = entry_select_bg, bd = 3,fg='#575757',relief='solid')

    b=Button(frame,text = "Get the details",bd=3, background=b_bg,relief='solid',font=f,
            highlightcolor=b_bg,foreground=b_fg,command=sql, highlightthickness=2)
    e.focus()
    e.bind('<Return>',lambda a:b.focus_set())
    e.bind('<Down>',lambda a:b.focus_set())
    b.bind('<Return>',lambda a:b.invoke())
    b.bind('<Up>',lambda a:e.focus_set())
    Grid.columnconfigure(frame,0,weight=1)
    Grid.rowconfigure(frame,0,weight=1)
    
    l1.grid(row=0,pady=10,padx=10,sticky='nsew')
    l2.grid(row=1,pady=10,padx=10,sticky='nsew')
    e.grid(row=0,column=1,pady=10,padx=10,sticky='nsew',ipadx=5)
    b.grid(row=1,column=1,padx=10,pady=10,sticky='nsew')

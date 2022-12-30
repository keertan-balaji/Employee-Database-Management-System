from tkinter import *
from tkinter import ttk 
import mysql.connector,textwrap
from mysql.connector import Error
from tkinter import *
from PIL import Image, ImageTk
from time import sleep
#stats = [b_fg,b_bg,background,f,entry_bg,label_fg,entry_select_bg,sql_u,sql_p]
def run(stats):
    b_fg=stats[0]; b_bg=stats[1]
    background=stats[2]
    f=list(stats[3])
    f[1]=18
    f=tuple(f)
    entry_bg=stats[4]; label_fg=stats[5]
    entry_select_bg=stats[6]
    sql_u=stats[7]; sql_p=stats[8]

    w = Tk()
    w.configure(bg = 'black')
    w.title("EmployeeDBManagement: Employees Details (Salary-based)")
    w.focus_force()
    w.resizable(False,False)
    w.iconbitmap('emp_salarybased.ico')
    
    def error():
        w.attributes('-topmost',True)
        messagebox.showerror("Error","Invalid Salary")
        w.attributes('-topmost',False)
        w.focus_force()
        del_b.focus()

    def dis():
        be=round(begin.get(),0)
        en=round(end.get(),0)
        for i in range(9):
            if len(str(be))==i:
                be='0'*(9-i)+str(be)
            if len(str(en))==i:
                en='0'*(9-i)+str(en)
        begin_l.configure(text='From: '+be)
        end_l.configure(text='To   : '+en)
        begin_l.update()
        end_l.update()
    
    def display():
        global cursor,db,count
        a = str(begin.get()); b = str(end.get())
        cond = [a,b]
        if cond:
            query = "select * from employee where salary between {} and {};".format(a,b)
            cursor.execute(query)
            rec = cursor.fetchall()
            for selected_item in table.get_children(): table.delete(selected_item)
            if count==0:
                #w.geometry('666x475')
                w.geometry('680x540')
                w.maxsize(680,540)
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
                i=list(i)
                i[3]='\n'.join(textwrap.wrap(i[3],25))
                i=tuple(i)
                table.insert('','end',values=i,open=True)
            count+=1
            w.resizable(True,True)
            table.pack(expand=True,fill=BOTH,pady=5,padx=5)
        else: error()
    global frame1,frame2,cursor,db,count
    db = mysql.connector.connect(host = "localhost", database = 'edms',user = sql_u,password = sql_p)
    cursor = db.cursor()
    count = 0
    fr=Frame(w,bg=background)
    fr.pack(padx=5,pady=5,expand=True,fill=BOTH)
    frame1=Frame(fr,bg=background)
    frame1.pack(padx=10,pady=10,fill=BOTH,expand=True)
    frame2=Frame(fr,bg=background,width=10,height=10)
    frame2.pack(padx=10,pady=10,fill=BOTH,expand=True)

    table=ttk.Treeview(frame1,padding=(4,5,10,10))
    xscroll_bar=ttk.Scrollbar(frame1,orient='horizontal',command=table.xview)
    yscroll_bar=ttk.Scrollbar(frame1,orient='vertical',command=table.yview)

    table.configure(xscrollcommand=xscroll_bar.set)
    table.configure(yscrollcommand=yscroll_bar.set)

    """ Connect to MySQL database """
    query2 = "select max(salary) from employee;" 
    cursor.execute(query2) 
    desigs = cursor.fetchall()
    maxsal = desigs[0][0]
    global begin, end

    wel=Label(frame2,text='''Select the range of salary for which
you want to view the records for:''',background = background, foreground = label_fg, font = f,anchor='center')
    wel.grid(padx = 75, pady = 5, row = 0, column = 0,columnspan = 2,sticky='nsew')

    begin = ttk.Scale(frame2,from_= 0, to = maxsal, orient = HORIZONTAL, length = 300,command=lambda e:dis())
    begin.grid(padx = 20, pady = 5, row = 1, column = 1, columnspan = 2,sticky='nsew')

    end = ttk.Scale(frame2,from_= 0, to = maxsal, orient = HORIZONTAL, length = 300,command=lambda e:dis())
    end.grid(padx = 20, pady = 5, row = 2, column = 1, columnspan = 2,sticky='nsew')

    begin_l =Label(frame2,text='From: 000000.0', background = background, foreground = label_fg, font = f)
    begin_l.grid(padx = 20, pady = 5, row = 1, column = 0,sticky='nsew')

    end_l = Label(frame2,text='To   : 000000.0', background = background, foreground = label_fg, font = f)
    end_l.grid(padx = 20, pady = 5, row = 2, column = 0,sticky='nsew')

    del_b = Button(frame2,bd=3,text='Reshow the table',
             background=b_bg,relief='solid',font=f,
             activebackground=b_bg,wraplength=290,
             highlightbackground='blue',command = display)
    
    del_b.grid(padx = 20, pady = 5, row = 3, column = 1, columnspan = 2,sticky='nsew')
    del_b.focus()
    Grid.columnconfigure(frame2,0,weight=1)
    Grid.rowconfigure(frame2,0,weight=1)
    del_b.bind('<Left>',lambda e:drop.focus_set())
    del_b.bind('<Return>',lambda e:del_b.invoke())
    mainloop()

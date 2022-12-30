from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def run(stats):
    b_fg=stats[0]; b_bg=stats[1]
    background=stats[2]
    f=list(stats[3])
    f[1]=18
    f=tuple(f)
    entry_bg=stats[4]; label_fg=stats[5]
    entry_select_bg=stats[6]
    sql_u=stats[7]; sql_p=stats[8]

    global count
    count=0
    def error():
        messagebox.showerror("Error","Invalid Employee ID")
        w.attributes('-topmost',True)
        w.attributes('-topmost',False)
        w.focus_force()
            
    def callback():
        global count; a=e.get()
        try:
            
            if int(a) not in idlist: error()
            else:
                sql="SELECT * FROM EMPLOYEE WHERE emp_id={0}".format(a,)
                mycursor.execute(sql)
                details=mycursor.fetchall()
                if count!=0:
                    for selected_item in table.get_children(): table.delete(selected_item)
                if count==0:
                    columns=['EMPLOYEE ID','NAME','DOB','ADDRESS','BANK ACCOUNT NUMBER','PAN CARD NUMBER',
             'DESIGNATION','DEPARTMENT','REPORTING MANAGER','EARNED LEAVE',
             'PAID LEAVE','SALARY','NET PAY','INCOME TAX','BONUS']
                    table['columns']=columns
                    for i in columns:
                        table.heading(i,text=i)
                        table.column(i,stretch=YES,anchor='center',minwidth=300)
                    table.column('#0',width=1,stretch=NO)
                    '''To remove the default column which is of no use to us
                    since we can not put any values in this column'''
                for i in details: table.insert('','end',values=i)
                xscroll_bar.pack(side=BOTTOM,fill=X)
                yscroll_bar.pack(side=RIGHT,fill=Y)
                table.pack(expand=True,fill=BOTH,padx=4,pady=4)
                frame.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky='nsew')
                count+=1
        except: error()

    mydb=mysql.connector.connect(host="localhost",user=sql_u, passwd=sql_p,database="edms")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT emp_id FROM EMPLOYEE")
    idraw=mycursor.fetchall()
    idlist=[]
    for i in idraw: idlist.append(i[0])


    w = Tk(); w.maxsize(1000,500)
    w.title('EmployeeDBManagement: One Employee\'s Details')
    w.focus_force(); w.configure(bg='black')
    w.iconbitmap('emp_details1.ico')
    
    fr=Frame(w,bg=background)
    fr.pack(padx=4,pady=4,fill=BOTH,expand=True)
    Grid.columnconfigure(fr,0,weight=1)
    Grid.rowconfigure(fr,0,weight=1)
    ft=list(f)
    ft=[ft[0]]+[12]+['']
    frame=Frame(fr,bg='black')
    ttk.Style().configure("Treeview",font=ft) # Modify the font of the body
    ttk.Style().configure("Treeview.Heading", font=f) # Modify the font of the headings

    table=ttk.Treeview(frame)
    columns=['Emp_id','name','DOB','address','bank_ac','pan_no','designation','department'
         ,'reporting_manager','el','pl','salary','netpay','itax','bonus']

    table['style']='Treeview'

    xscroll_bar=ttk.Scrollbar(frame,orient='horizontal',command=table.xview)
    yscroll_bar=ttk.Scrollbar(frame,orient='vertical',command=table.yview)

    table.configure(xscrollcommand=xscroll_bar.set)
    table.configure(yscrollcommand=yscroll_bar.set)

    l1=Label(fr,text="Enter Employee id:",font = f, fg = label_fg,bg = background)
    l1.grid(row=1,padx=5,pady=5,sticky='ew')

    e = Entry(fr,bg = entry_bg,font = f, selectbackground = entry_select_bg,
              bd = 5,fg='#575757',relief='solid')
    e.grid(row=1,column=1,padx=5,pady=5,sticky='nsew')

    b=Button(fr,text='Show the details',background=b_bg,relief='solid',font=f,
        activebackground=b_bg,bd=3,foreground=b_fg,
        highlightbackground='blue',command=callback)
    e.focus()
    e.bind('<Return>',lambda e:b.focus_set())
    e.bind('<Down>',lambda e:b.focus_set())
               
    b.grid(row=2,columnspan=2,padx=5,pady=5,sticky='nsew')
    b.bind('<Up>',lambda g:e.focus())
    b.bind('<Return>',lambda g:b.invoke())
    mainloop()

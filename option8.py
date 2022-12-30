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

        def error():
                messagebox.showerror("Error","Invalid Employee ID")
                w.attributes('-topmost',True)
                w.focus_force()
                w.attributes('-topmost',False)
                e1.focus()

        def success():
                messagebox.showinfo("Success","Employee Data Removed Successfully")
                w.attributes('-topmost',True)
                w.focus_force()
                w.attributes('-topmost',False)
                e1.focus()
                
        def callback():
                def yes():
                    top.destroy()
                    modsql='delete from employee where emp_id={0}'.format(a)
                    mycursor.execute(modsql)
                    mydb.commit()
                    success()
                    w.attributes('-topmost',True)
                    w.focus_force()
                    w.attributes('-topmost',False)
                    b2.focus()
                mycursor.execute("SELECT emp_id FROM EMPLOYEE")
                idraw=mycursor.fetchall()
                idlist=[]
                for i in idraw: idlist.append(i[0])
                global top,a
                a=e1.get()
                if int(a) not in idlist: error()
                else:
                    top=Tk()
                    top.configure(bg='black')
                    top.title('Confirmation:')
                    w.attributes('-topmost',True)
                    w.focus_force()
                    w.attributes('-topmost',False)
                    top.iconbitmap('emp_delete.ico')
                    fr=Frame(top,bg=background)
                    l=Label(fr,text='Are You sure u want to delete the record??',font=f,
                                fg = label_fg,bg = background,
                                height = 1,wraplength=300).pack(ipady=10,padx=5,pady=10,expand=True,fill=BOTH)
                    b2=Button(fr,text='NO',bd=3,background=b_bg,
                    relief='solid',font=f,activebackground=b_bg,
                    wraplength=290,highlightcolor='blue',
                              command=top.destroy)
                    b2.pack(padx=5,pady=5,expand=True,fill=BOTH,side='left')
                    b1=Button(fr,text='YES',bd=3,background=b_bg,
                    relief='solid',font=f,activebackground=b_bg,
                    wraplength=290,highlightcolor='blue',
                    command=yes)
                    b1.pack(padx=5,pady=5,expand=True,fill=BOTH,side='left')
                    
                    fr.pack(padx=5,pady=5,expand=True,fill=BOTH)
                    b2.focus_set()
                    top.mainloop()
        mydb=mysql.connector.connect(host="localhost",user=sql_u, passwd=sql_p,database="edms")
        mycursor=mydb.cursor()
        w=Tk()
        w.title("EmployeeDBManagement: Delete Employee Records")
        w.configure(bg='black')
        w.iconbitmap('emp_delete.ico')
        w.focus_force()

        frame=Frame(w,bg=background)
        frame.pack(padx=5,pady=5,expand=True,fill=BOTH)

        Grid.columnconfigure(frame,0,weight=1)
        Grid.rowconfigure(frame,0,weight=1)

        lb1=Label(frame, text="Enter Employee ID:",font = f, fg = label_fg,bg = background,
                height = 1,wraplength=300).grid(row=0,column=0,padx=5,pady=5)

        columns=["Name","DOB","Address","bank_ac","pan_no","Designation","Department",
                 "Reporting_manager","el","pl","Pay"]

        
        e1 = Entry(frame,bg = entry_bg,font = f, 
            selectbackground = entry_select_bg, bd = 5,relief='solid')

        e1.grid(row=0,column=1,padx=5,pady=5,sticky='nsew')

        b = Button(frame,text="Delete",bd=3,background=b_bg,
                   relief='solid',font=f,activebackground=b_bg,
                   wraplength=290,highlightcolor='blue',
                   command=callback)
        b.grid(row=4,column=0,padx=5,pady=5,columnspan=2,sticky='nsew')

        e1.focus()
        e1.bind('<Return>',lambda e:b.focus_set())
        e1.bind('<Down>',lambda e:b.focus_set())
        b.bind('<Return>',lambda e:b.invoke())
        b.bind('<Up>',lambda e:e1.focus_set())

        mainloop()

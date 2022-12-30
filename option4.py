from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from datetime import date

def run(stats):
        b_fg=stats[0]; b_bg=stats[1]
        background=stats[2]
        f=list(stats[3])
        f[1]=18
        f=tuple(f)
        entry_bg=stats[4]; label_fg=stats[5]
        entry_select_bg=stats[6]
        sql_u=stats[7]; sql_p=stats[8]


        def success():
                messagebox.showinfo("Success","Employee Data Modified Successfully")
                w.attributes('-topmost',True)
                w.focus_force()
                w.attributes('-topmost',False)
                e1.focus()

        def check(a,b,c):
                k=None
                finaltext=[]
                j=''.join(b.strip().split())

                if a=='':finaltext.append('Please fill the ID box')
                if c=='':finaltext.append('Please select the column to want modify')
                elif not(a.isdigit()):
                        finaltext.append('Wrong ID,ID has to be a number')
                elif int(a) not in idlist:
                        finaltext.append('This Employee ID dosent exist')

                if b=='':finaltext.append('Please Enter the value you want to modify')
                elif c==columns[0]:
                        k=0
                        if not(j.isalpha()):
                                finaltext.append('Name field can have only spaces and alphabets!!')
                elif c==columns[5]:
                        k=5
                        if not(j.isalpha()):
                                finaltext.append('Designation field can have only spaces and alphabets!!')
                elif c==columns[7]:
                        k=7
                        if not(j.isalpha()):
                                finaltext.append('Reporting manager field can have only spaces and alphabets!!') 
                elif c==columns[1]:
                        k=1
                        today = date.today()
                        s1=today.strftime("%Y-%m-%d")
                        d1=s1.split('-')
                        ff=b.strip().split('-')
                        z1=not(ff[0].isdigit() and len(ff[0])==4)
                        z2=not(ff[1].isdigit()and len(ff[1])==2)
                        z3=not(ff[2].isdigit() and len(ff[2])==2)
                        print(ff,z1,z2,z3)
                        if len(ff)!=3 or (z1 or z2 or z3):
                                finaltext.append('''Date of birth should have only digits and
        should be of the form YYYY-MM-DD !!''')
                        else:
                                ch1=int(ff[0])<=1920 or int(ff[0])>=int(d1[0])
                                ch2=(int(ff[1])<1 and int(ff[1])>12) or int(ff[1])>int(d1[1])
                                ch3=(int(ff[2])<1 and int(ff[2]>31))or int(ff[2])>int(d1[2])
                                print(ch1,ch2,ch3)
                                if ch1 or ch2 or ch3:
                                        finaltext.append('''Please enter valid DOB,only dates after
1920 and before '''+s1+' accepted')
                                
                elif c==columns[2]:
                        k=2
                        check2=None
                        for i in b:
                            if not(i.isalnum()) and (i not in [',','/','#','-',' ','\n']): check2=True
                        if check2:
                            finaltext.append('''Address field can have only alphabets,numbers and special
symbols , # / and - ''')
                elif c==columns[3]:
                        k=3
                        if not(b.isdigit()) or len(b)!=26:
                            finaltext.append('''Bank account should have 26 digits
combination of numbers!!''')
                elif c==columns[4]:
                        k=4
                        j1=not(b[:5].isalpha())
                        j2=not(b[5:len(b)-1].isdigit)
                        j3=not(b[-1].isalpha())
                        j4=len(b)!=10
                        print(j1,j2,j3,j4)
                        if j1 or j2 or j3 or j4:
                            finaltext.append('''Pan number has to have at least 10 characters first
5 being capitalized letters,then next 4 numbers and then the last character an alphabet!!!''')
                elif c==columns[6]:
                        k=6
                        if not(b.strip().isalnum()): finaltext.append('Department field can have only alphabets and numbers!!')
                elif c==columns[8]:
                        k=8
                        if not(b.strip().isdigit()):
                                finaltext.append('Earned Leave field can have only 2 digit numbers less than 18!!')
                elif c==columns[9]:
                        k=9
                        if not(b.strip().isdigit()):
                                finaltext.append('Paid Leave field can have only 2 digit numbers less than 15!!')
                elif c==columns[10]:
                        k=10
                        if not(b.strip().isdigit()) or len(b)>7:
                            finaltext.append('Salary can have only 7 digits, i.e. only numbers allowed!!')
                if finaltext==[]: return [True,k]
                else:
                    messagebox.showerror('Error :(','\n\n'.join(finaltext))
                    w.attributes('-topmost',True)
                    w.attributes('-topmost',False)
                    w.focus_force()
                    return [False,k]
        def callback():
                a1=e1.get()#id
                b1=e2.get()#Modified value
                c1=dp1.get()#the column to be modified
                j=check(a1,b1,c1)
                if j[0]==True:                        
                        if c1==columns[10]:
                            taxmod=int(0.15*int(b1))
                            netmod=int(b1)-taxmod   
                            modsql="UPDATE EMPLOYEE SET {0}={1},itax={2},netpay={3} WHERE emp_id={4}".format(sql_columns[j[1]+1],b1,taxmod,netmod,a1)
                        else: modsql="UPDATE EMPLOYEE SET {0}='{1}' WHERE emp_id={2}".format(sql_columns[j[1]+1],b1,a1)
                        mycursor.execute(modsql)
                        mydb.commit()
                        success()
        mydb=mysql.connector.connect(host="localhost",user=sql_u, passwd=sql_p,database="edms")
        mycursor=mydb.cursor()
        mycursor.execute("SELECT emp_id FROM EMPLOYEE")
        idraw=mycursor.fetchall()
        idlist=[]
        for i in idraw: idlist.append(i[0])
        w=Tk()
        w.title("EmployeeDBManagement: Modify Employee Details")
        w.configure(bg='black')
        w.iconbitmap('emp_modify.ico')
        w.focus_force()

        frame=Frame(w,bg=background)
        frame.pack(padx=5,pady=5,expand=True,fill=BOTH)

        Grid.columnconfigure(frame,0,weight=1)
        Grid.rowconfigure(frame,0,weight=1)

        lb1=Label(frame, text="Enter Employee ID:",font = f, fg = label_fg,bg = background,
                            height = 1,wraplength=300).grid(row=0,column=0,padx=5,pady=5)
        sql_columns=['emp_id','name','DOB','address','bank_ac','pan_no','designation',
                     'department','reporting_manager','el','pl','salary','netpay','itax',
                     'bonus']
        columns=['NAME','DOB','ADDRESS','BANK ACCOUNT NUMBER','PAN CARD NUMBER',
             'DESIGNATION','DEPARTMENT','REPORTING MANAGER','EARNED LEAVE',
             'PAID LEAVE','SALARY']
        lb2=Label(frame, text="Select The column To Be Modified:",font = f,
                            fg = label_fg,bg = background
                  ,wraplength=200).grid(row=1,column=0,padx=5,pady=5,sticky='nsew')
        ft=(f[0],18,f[2])
        style=ttk.Style().configure('TCombobox',font=f,bg='red')
        frr=Frame(frame,bg='black')
        dp1=ttk.Combobox(frr,font=ft)
        dp1.pack(fill=BOTH,expand=True,padx=4,pady=4)
        frr.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
        dp1['values']=columns
        lb3=Label(frame, text="Enter New Value:",font = f, fg = label_fg,bg = background,
                            wraplength=250).grid(row=3,column=0,padx=5,pady=5,sticky='nsew')

        e1 = Entry(frame,bg = entry_bg,font = f, selectbackground = entry_select_bg,
                bd = 5,relief='solid')
        e2 = Entry(frame,bg = entry_bg,font = f,
                    selectbackground = entry_select_bg,
                    bd = 5,relief='solid')
        e1.grid(row=0,column=1,padx=5,pady=5,sticky='nsew')
        e2.grid(row=3,column=1,padx=5,pady=5,sticky='nsew')

        b = Button(frame,text="Modify",bd=3,background=b_bg,
                   relief='solid',font=f,activebackground=b_bg,
                   wraplength=290,highlightcolor='blue',
                   command=callback)
        b.grid(row=4,column=0,padx=5,pady=5,columnspan=2,sticky='nsew')

        e1.focus()
        e1.bind('<Return>',lambda e:dp1.focus_set())
        e1.bind('<Down>',lambda e:dp1.focus_set())
        dp1.bind('<Return>',lambda e:e2.focus_set())
        dp1.bind('<Up>',lambda e:e1.focus_set())
        e2.bind('<Return>',lambda e:b.focus_set())
        e2.bind('<Up>',lambda e:dp1.focus_set())
        e2.bind('<Down>',lambda e:b.focus_set())
        b.bind('<Return>',lambda e:b.invoke())
        b.bind('<Up>',lambda e:e2.focus_set())

        mainloop()

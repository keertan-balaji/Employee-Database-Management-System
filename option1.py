from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from datetime import date

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

    def check(rec):
        finaltext=[]
        db = mysql.connector.connect(host = "localhost", database = 'edms', 
                user = sql_u, password = sql_p)
        cursor = db.cursor()
        cursor.execute('select emp_id from employee')
        idlist=cursor.fetchall()
        print(idlist)
        for i in [1,6,8]:
            j=''.join(rec[i].strip().split())    
            if not(j.isalpha()):
                if i==1: finaltext.append('Name field can have only spaces and alphabets!!')
                elif i==6: finaltext.append('Designation field can have only spaces and alphabets!!')
                elif i==8: finaltext.append('Reporting manager field can have only spaces and alphabets!!')
        a=rec[0].strip()
        if not(a.isdigit()):
            finaltext.append('Wrong ID,ID has to be a number')
        elif (int(a),)in idlist:
            finaltext.append('This Employee ID exists please enter a new employee ID')
        ff=rec[2].strip().split('-')
        today = date.today()
        s1=today.strftime("%Y-%m-%d")
        d1=s1.split('-')
        z1=not(ff[0].isdigit() and len(ff[0])==4)
        z2=not(ff[1].isdigit()and len(ff[1])==2)
        z3=not(ff[2].isdigit() and len(ff[2])==2)
        print(ff,z1,z2,z3)
        if len(ff)!=3 or (z1 or z2 or z3):
            finaltext.append('''Date of birth should have only digits and
should be of the form YYYY-MM-DD !!''')
        else:
            ch1=int(ff[0])<=1920 or int(ff[0])>=int(d1[0])
            ch2=1>int(ff[1])>12 or int(ff[1])>int(d1[1])
            ch3=(31<int(ff[2])<1)or int(ff[2])>int(d1[2])
            print(ch1,ch2,ch3)
            if ch1 or ch2 or ch3:
                finaltext.append('''Please enter valid DOB,only dates after
1920 and before '''+s1+' accepted')
                       
        if not(rec[3].isdigit()) or len(rec[3])!=26:
            finaltext.append('''Bank account should have 26 digits
combination of numbers!!''')
        j1=not(rec[4][:5].isalpha())
        j2=not(rec[4][5:len(rec[4])-1].isdigit)
        j3=not(rec[4][-1].isalpha())
        j4=len(rec[4])!=10
        print(j1,j2,j3,j4)
        if j1 or j2 or j3 or j4:
            finaltext.append('''Pan number has to have at least 10 characters first
5 being capitalized letters,then next 4 numbers and then the last character an alphabet!!!''')
        check2=None
        for i in rec[5]:
            if not(i.isalnum()) and (i not in [',','/','#','-',' ','\n']): check2=True
        if check2:
            finaltext.append('''Address field can have only alphabets,numbers and special
symbols , # / and - ''')
        if not(rec[7].strip().isalnum()): finaltext.append('Department field can have only alphabets and numbers!!')
        for i in [9,10]:
            if not(rec[i].strip().isdigit()):
                if i==9: finaltext.append('Earned Leave field can have only 2 digit numbers less than 18!!')
                elif i==10: finaltext.append('Paid Leave field can have only 2 digit numbers less than 15!!')
        if not(rec[11].strip().isdigit()) or len(rec[11])>7:
                            finaltext.append('Salary can have only 7 digits, i.e. only numbers allowed!!')
        if finaltext==[]: return True
        else:
            messagebox.showerror('Error :(','\n\n'.join(finaltext))
            w.attributes('-topmost',True)
            w.attributes('-topmost',False)
            w.focus_force()
    def success():
        messagebox.showinfo("Success",'Record Entered')
        w.attributes('-topmost',True)
        w.attributes('-topmost',False)
        w.focus_force()
    def connect(record):
        """ Connects to MySQL database """
        try:
            global db; db=None
            db = mysql.connector.connect(host = "localhost", database = 'edms', 
                user = sql_u, password = sql_p)
            cursor = db.cursor()
            insertsql= '''INSERT INTO EMPLOYEE (emp_id,name,DOB,bank_ac,pan_no,address,designation,department,reporting_manager, el, pl, salary,netpay, itax,bonus)
VALUES({0},'{1}','{2}',{3},'{4}','{5}','{6}','{7}','{8}',{9},{10},{11},{12},{13},{14})'''.format(
            record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14])
            print(record,insertsql)
            cursor.execute(insertsql)
            db.commit()            
            cursor.close()
            success()
        except Error as err:
            messagebox.showerror("Error",str(err))
            w.attributes('-topmost',True)
            w.attributes('-topmost',False)
            w.focus_force()
            return True
    def error():
        messagebox.showerror("Error",'Please fill All fields  :)')
        w.attributes('-topmost',True)
        w.attributes('-topmost',False)
        w.focus_force()
    def recall():
        try:
            rec = values = []
            for i in range(11):entries[i].update()
            for i in range(11):
                if i==5:
                    values.append(text.get('1.0',END))
                e=str(entries[i].get()).strip()
                values.append(e)
            
            if '' in values: error()
            else:
                val=check(values)
                values[0]=int(values[0])
                tax=int(0.15*int(values[-2]))
                netpay=int(values[-2])-tax
                values.extend([netpay,tax,netpay*0.1])
                values[11]=float(values[11])
                values[10]=int(values[10])
                values[9]=int(values[9])
                values[3]=int(values[3])
                values[5]=' '.join(values[5].split('\n'))
                values=tuple(values)
                j=False
                if val and j==False: j=connect(values)
        except:
            pass
    w=Tk(); w.configure(bg ='black')
    w.title("EmployeeDBManagement: Entering Records Into Database")
    w.iconbitmap('emp_add.ico')
    w.focus_force(); w.geometry('1180x540')
    w.minsize(1180,540)
    frame=Frame(w,bg=background)
    frame.pack(padx=5,pady=5,fill=BOTH,expand=True)
    text=['Employee ID:','Name:','Date Of Birth:','Bank Account:','Pan Number:',
          'Designation:','Department:','Reporting Manager:',
          'Earned Leave:','Paid Leave:','Salary:','Address:']

    Grid.columnconfigure(w,0,weight=1)
    Grid.rowconfigure(w,0,weight=1)
    
    labels=[]; r=c=0
    for i in range(12):
        label=Label(frame,text='Employee '+text[i],font = f,
                    fg = label_fg,bg = background).grid(row = r,column = c,ipadx = 10,sticky='nsew')
        labels.append(label)
        Grid.columnconfigure(frame,i,weight=1)
        Grid.rowconfigure(frame,i,weight=1)
        if r==5: c=2; r=0
        else: r+=1

    b = Button(frame, text = "Enter the records into the database",
               background=b_bg,relief='solid',font=f,
               activebackground=b_bg,foreground=b_fg,
               command = recall)
    
    b.grid(row = 16,column =0,columnspan = 4,pady=5,padx=5,sticky='nsew')
    
    entries=[]; rno=0; cno=1
    for i in range(11):
        entry=Entry(frame,bg = entry_bg,font = f,
                    selectbackground = entry_select_bg
                    ,bd = 5,fg='#575757',relief='solid')
        entry.grid(row = rno,column = cno,
                   ipadx = 20,ipady = 10,
                   padx=6,pady=5,sticky='nsew')
        
        Grid.columnconfigure(frame,i,weight=1)
        Grid.rowconfigure(frame,i,weight=1)
        if rno==5: cno=3; rno=0
        else: rno+=1
        entries.append(entry)
    pretext=['Enter ID','Enter Name','YYYY-MM-DD','XXXXXXXXXXXX',
             'Eg:- ABE4124232']
    for i in range(4):
        entries[i].insert(0,pretext[i])
    text=Text(frame,bg = entry_bg,font = f,
                    selectbackground = entry_select_bg
                    ,bd = 5,fg='#575757',relief='solid',wrap='word')
    yscrollbar = ttk.Scrollbar(text,orient="vertical", command=text.yview)
    yscrollbar.pack(side="right", fill="y")
    text.configure(yscrollcommand=yscrollbar.set)
    text.grid(row = 5,column = 3, ipadx = 20,ipady = 10, padx=6,pady=5,sticky='nsew')
    
    entries[0].focus()
    entries[0].bind('<Return>',lambda e:entries[1].focus_set())
    entries[0].bind('<Down>',lambda e:entries[1].focus_set())
    entries[1].bind('<Return>',lambda e:entries[2].focus_set())
    entries[1].bind('<Up>',lambda e:entries[0].focus_set())
    entries[1].bind('<Down>',lambda e:entries[2].focus_set())
    entries[2].bind('<Return>',lambda e:entries[3].focus_set())
    entries[2].bind('<Up>',lambda e:entries[1].focus_set())
    entries[2].bind('<Down>',lambda e:entries[3].focus_set())
    entries[3].bind('<Return>',lambda e:entries[4].focus_set())
    entries[3].bind('<Up>',lambda e:entries[2].focus_set())
    entries[3].bind('<Down>',lambda e:entries[4].focus_set())
    entries[4].bind('<Return>',lambda e:entries[5].focus_set())
    entries[4].bind('<Down>',lambda e:entries[5].focus_set())
    entries[4].bind('<Up>',lambda e:entries[3].focus_set())
    entries[5].bind('<Return>',lambda e:entries[6].focus_set())
    entries[5].bind('<Down>',lambda e:entries[6].focus_set())
    entries[5].bind('<Up>',lambda e:text.focus_set())
    entries[6].bind('<Return>',lambda e:entries[7].focus_set())
    entries[6].bind('<Down>',lambda e:entries[7].focus_set())
    entries[6].bind('<Up>',lambda e:entries[5].focus_set())
    entries[7].bind('<Return>',lambda e:entries[8].focus_set())
    entries[7].bind('<Down>',lambda e:entries[8].focus_set())
    entries[7].bind('<Up>',lambda e:entries[6].focus_set())
    entries[8].bind('<Down>',lambda e:entries[9].focus_set())
    entries[8].bind('<Up>',lambda e:entries[7].focus_set())
    entries[8].bind('<Return>',lambda e:entries[9].focus_set())
    entries[9].bind('<Up>',lambda e:entries[8].focus_set())
    entries[9].bind('<Down>',lambda e:entries[10].focus_set())
    entries[9].bind('<Return>',lambda e:entries[10].focus_set())
    entries[10].bind('<Return>',lambda e:text.focus_set())
    entries[10].bind('<Up>',lambda e:entries[9].focus_set())
    entries[10].bind('<Down>',lambda e:text.focus_set())
    b.bind('<Return>',lambda e:b.invoke())
    b.bind('<Up>',lambda e:text.focus_set())
    mainloop()

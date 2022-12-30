import mysql.connector

def checking(u,p,sql_username,sql_password):

    sql_u=sql_username
    sql_p=sql_password

    def hashing(mi): #Hashing algorithm
        s1, s2 = 1, 2
        dp = ""
        d = ['Bl$', '31!', 'fR#', 'VW@']
        e = ['@#2', '#$1', '#31', ':?|12', '$#@']
        for i in range(len(mi)):
            temp = s2
            s2 = s2 + s1
            s1 = temp
            if mi[i].isalpha():
                if mi[i].isupper():
                    if s2 % 2 == 0 or s2 == 1:
                        dp = dp + mi[i].lower() + d[0]
                    elif s2 % 3 == 0:
                        dp = dp + mi[i].lower() + d[1]
                    elif s2 % 4 == 0:
                        dp = dp + mi[i].lower() + d[2]
                    elif s2 % 5 == 0:
                        dp = dp + mi[i].lower() + d[3]
                else :
                    if s2 % 2 == 0 or s2 == 1:
                        dp = dp + mi[i].upper() + d[0]
                    elif s2 % 3 == 0:
                        dp = dp + mi[i].upper() + d[1]
                    elif s2 % 4 == 0:
                        dp = dp + mi[i].upper() + d[2]
                    elif s2 % 5 == 0:
                        dp = dp + mi[i].upper() + d[3]

            elif mi[i].isdigit():
                if s2 % 2 == 0 or s2 == 1:
                    dp = dp + mi[i] + e[0]
                elif s2 % 3 == 0:
                    dp = dp + mi[i] + e[1]
                elif s2 % 4 == 0:
                    dp = dp + mi[i] + e[2]
                elif s2 % 5 == 0:
                    dp = dp + mi[i] + e[3]
                else :
                    dp = dp + mi[i] + e[4]
            else :
                dp = dp + mi[i]
            return dp
    password=hashing(p)
    mydb=mysql.connector.connect(host='localhost',user=sql_u,password=sql_p)
    cursor=mydb.cursor()
    cursor.execute('show databases')
    gg=cursor.fetchall()
    if ('edms') in gg:
        query='SELECT password FROM SECURITY WHERE username="%s"'%(u)
        cursor.execute(query)
        rec=cursor.fetchall()
        cursor.close()
        if rec!=[]:
            if rec[0][0]==password:
                return True
            else:
                return False
        else:
            return 'Username does not exist'
    else:
        if password=='1#$1' or password=='R31!':
            return True
        else:
            return False

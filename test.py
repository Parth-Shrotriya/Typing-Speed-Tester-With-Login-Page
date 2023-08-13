from email import message
import pymysql
import smtplib as smtp
from tkinter import messagebox

#con=pymysql.connect(host='localhost',user='root',password='',database="employe")
#cur=con.cursor()
#cur.execute("select umail from data where umail=%s",("arjunshrotriya12@gmail.com"))
con=pymysql.connect(host='localhost',user='root',password='',database="employe")
cur=con.cursor()
cur.execute("select uemail from data where uemail=%s",("paarthshrotriya12@gmail.com"))
row1=cur.fetchone()
row3=str(row1)

con=pymysql.connect(host='localhost',user='root',password='',database="employe")
cur=con.cursor()
cur.execute("select upass from data where uemail=%s",("paarthshrotriya12@gmail.com"))
row2=cur.fetchone()
row4=str(row2)

x=row3[2:]
y=x[:-3]

message=(row4)
sender="login.help2021@gmail.com"
epass="a321b654"
message
ob=smtp.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login(sender,epass)
subject="Password for Login request"
ob.sendmail(sender,y,message)
ob.quit







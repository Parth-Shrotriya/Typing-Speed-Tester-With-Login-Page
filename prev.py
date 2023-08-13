import builtins
from tkinter import*
from tkinter import messagebox
import pymysql
import smtplib as smtp

class Login:

    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYS")
        self.root.geometry("1080x720")
        self.root.resizable(False,False)
        self.root.configure(bg="cyan")


        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=100,y=100,height=500,width=500)


        title=Label(Frame_login,text="Login here",font=("impact",35,"bold"),fg="#AF3000",bg="white").place(x=150,y=50)
        descrip=Label(Frame_login,text="Enter Your Credential Here",font=("goudy old style",15,"bold","underline"),fg="#0081B0",bg="white").place(x=140,y=120)


        userLab=Label(Frame_login,text="Username",font=("goudy old style",15,"bold"),fg="#808080",bg="white").place(x=50,y=190)
        self.txt_user=Entry(Frame_login,font=("Times new roman",15),bg="#D3D3D3")
        self.txt_user.place(x=50,y=215,width=350,height=35)


        userpass=Label(Frame_login,text="Password",font=("goudy old style",15,"bold"),fg="#808080",bg="white").place(x=50,y=260)
        self.txt_pass=Entry(Frame_login,font=("Times new roman",15),bg="#D3D3D3",show="*")
        self.txt_pass.place(x=50,y=285,width=350,height=35)

        forget=Button(Frame_login,command=self.forgetbtn,text="Forget Password",cursor="hand2",bg="White",fg="#0081B0",font=("Arial",10)).place(x=50,y=325)
        lognbut=Button(self.root,command=self.login_function,cursor="hand2",text="Login",bg="#0081B0",fg="white",font=("Arial",20))
        lognbut.place(x=350,y=500,width="150",height="40")
        regbut=Button(self.root,command=self.register_function,cursor="hand1",text="Register",bg="#0081B0",fg="white",font=("Arial",20))
        regbut.place(x=150,y=500,width="150",height="40")
    def clear(self):
        self.txt_pass.delete(0,END)
        self.txt_user.delete(0,END)


    def forgetbtn(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","Fields Incomplete",parent=self.root)
        else :
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database="employe")
                cur=con.cursor()
                cur.execute("select * from data where uemail=%s"
                            ,(self.txt_user.get()))


                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                    self.clear()
                else:
                    ob=smtp.SMTP("smtp.gmail.com",587)
                    ob.starttls()
                    ob.login("loginhelp.python@gmail.com","a3675u9sh")
                    subject="Password for Login request"
                    body=(
                        con=pymysql.connect(host='localhost',user='root',password='',database="employe")
                        
                    )
                    message="Subject:{}\n\n{}",format(subject,body)
                    listofaddress=(
                    n=pymysql.connect(host='localhost',user='root',password='',database="employe")
                        cur=con.cursor()
                        cur.execute("select * from data where uemail=%s"
                            ,(self.txt_user.get()))

                    )
                    ob.sendmail("loginhelp.python",listofaddress,message)
                    messagebox.showinfo("Success","Password has been sent to your registerd Email ID",parent=self.root)
                    ob.quit

                    


    
    







    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","Fields Incomplete",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database="employe")
                cur=con.cursor()
                cur.execute("select * from data where uemail=%s and upass=%s"
                            ,(self.txt_user.get(),self.txt_pass.get()))

                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                    self.clear()
                else:
                    self.newWindow =Toplevel(self.root)
                    self.app=window2(self.newWindow)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f'error Due to : {str(es)}'
                                    ,parent=self.root)
        
        #elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Parth":
            #messagebox.showerror("Error","Inval User ID/Pass",parent=self.root)
        #else:
           # self.newWindow =Toplevel(self.root)
            #self.app=window2(self.newWindow)
            

    def register_function(self):
        self.newWindow=Toplevel(self.root)
        self.app=register(self.newWindow)

    

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("700x700+0+0")
        self.root.resizable(False,False)
        self.root.configure(bg="cyan")

        Frame_register=Frame(self.root,bg="white")
        Frame_register.place(x=100,y=100,height=500,width=500)

        title=Label(Frame_register,text="REGISTER HERE",font=("times new roman",25,"bold"),bg="white",fg="black").place(x=50,y=30)

        self.var_fname=StringVar()
        fname=Label(Frame_register,text="Full Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=150)
        self.txt_fname=Entry(Frame_register,font=("times new roman",15),bg="light grey")
        self.txt_fname.place(x=50,y=175,width=250)

        uemail=Label(Frame_register,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=210)
        self.txt_uemail=Entry(Frame_register,font=("times new roman",15),bg="light grey")
        self.txt_uemail.place(x=50,y=235,width=250)

        upass=Label(Frame_register,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=270)
        self.txt_upass=Entry(Frame_register,font=("times new roman",15),bg="light grey")
        self.txt_upass.place(x=50,y=295,width=250)

        uxpass=Label(Frame_register,text="Confrim New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=330)
        self.txt_ucpass=Entry(Frame_register,font=("times new roman",15),bg="light grey")
        self.txt_ucpass.place(x=50,y=355,width=250)

        regibut=Button(Frame_register,text="REGISTER",font=("times new roman",15,"bold"),bg="white",fg="black",cursor="hand1",command=self.register_data).place(x=70,y=410,height="40",width=150)
    
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_uemail.delete(0,END)
        self.txt_upass.delete(0,END)
        self.txt_ucpass.delete(0,END)


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_uemail.get()=="" or self.txt_upass.get()=="" or self.txt_ucpass.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root)

        elif self.txt_upass.get()!=self.txt_ucpass.get():
            messagebox.showerror("Error","Password does not match",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employe")
                cur=con.cursor()
                cur.execute("select * from data where uemail=%s",self.txt_uemail.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exist",parent=self.root)
                else:
                    cur.execute("insert into data (fname,uemail,upass) values(%s,%s,%s)",
                                (self.txt_fname.get(),
                                self.txt_uemail.get(),
                                self.txt_upass.get()


                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Regristration Done",parent=self.root)
                    self.clear()




        
            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

        



                

class window2:
    def __init__(self,root):
        self.root=root
        self.root.title("Application windows")
        self.root.geometry("1080x720")
        self.root.resizable(False,False)
        self.root.configure(bg="grey")
        self.frame=Frame(self.root,bg="white")





root=Tk()
obj=Login(root)
root.mainloop()
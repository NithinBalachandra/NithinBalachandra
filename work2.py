from tkinter import *
window=Tk()
window.title="work2"
window.geometry("900x500")
def Click1():
    
    user1=e1.get()
    password=e2.get()

    if "nithin"== user1 and "nithin123"== password:
        l5=Label(window,text="login successfully",font=("Arial",18),fg="green",bg="white")
        l5.grid(column=2,row=8)
    else:
        l6=Label(window,text="Invalid",font=("Arial",18),fg="red",bg="white")
        l6.grid(column=2,row=9)

l1=Label(window,text="Login",font=("Times New Roman bold",38),fg="white",bg="blue")
l3=Label(window,text="User name",font=("Arial",18),bg="white")
e1=Entry(window,width=45)
l4=Label(window,text="password",font=("Arial",18),bg="white")
e2=Entry(window,width=45)
b1=Button(window,text="Sign in",font=("Georgia Italic",18),fg="yellow",bg="green",command=Click1)


l1.grid(column=2,row=0)

l3.grid(column=1,row=4)
e1.grid(column=2,row=4)
l4.grid(column= 1,row=5)
e2.grid(column=2, row=5)
b1.grid(column=2,row=7)


window.configure(bg="white")

window.mainloop()


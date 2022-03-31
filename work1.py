import tkinter
from tkinter import font
from turtle import bgcolor
window=tkinter.Tk()
window.title("Python")
window.geometry("800x500")
l=tkinter.Label(window,text="Python",font=("Arial Bold Italic",30),fg="red",bg="white").pack()
l=tkinter.Label(window,text="""Python is an interpreted, object-oriented
high-level programming language with dynamic semantics Python's simple, 
easy to learn syntax emphasizes readability and therefore reduces the 
cost of program maintenance. Python supports modules and packages, 
which encourages program modularity and code reuse.""",font=("Monotype Corsiva",24),bg="white").pack()
l=tkinter.Label(window,text="""Guido van Rossum began working on Python in the late 1980s,
as a successor to the ABC programming language,
and first released it in 1991 as Python 0.9.0.[33] 
Python 2.0 was released in 2000 and introduced new features,
such as list comprehensions and a cycle-detecting garbage collection
system (in addition to reference counting). Python 3.0 was released 
in 2008 and was a major revision of the language that
is not completely backward-compatible. Python 2 was discontinued 
with version 2.7.18 in 2020.""",font=("Times New Roman",24),bg="white").pack()
window.configure(bg="white")
window.mainloop()


#import tkinter


#window=tkinter.Tk()
#window.title("Python")
#window.geometry("450x500")
#l=tkinter.Label(window,image="python.ppm").pack()
#l=tkinter.Image(window,image= r"C:\Users\Nithin\Desktop\python.png")
#window.mainloop()"""


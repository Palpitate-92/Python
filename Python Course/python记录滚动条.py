from tkinter import *
w=Tk()
w.geometry("200x80")
d=Tk()
draw=Canvas(d,width=200,height=500)
x=100
y=0
def show(text):
    global x,y
    draw.create_line(x,y,2*float(v.get()),y+3)
    x=2*float(v.get())
    if y>500:
        y=0
    else: 
        y+=1
    print("v=",v.get())
def clear():
    global y
    for obj in draw.find_withtag("all"):
        draw.delete(obj)
    y=0
v=StringVar()
scl=Scale(w,from_=0,to=100,resolution=0.1,orient=HORIZONTAL,variable=v,command=show)
scl.set(50)
b=Button(w,text="clear",command=clear)
scl.pack()
b.pack()
draw.pack()
w.mainloop()

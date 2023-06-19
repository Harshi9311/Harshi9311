from tkinter import*
import qrcode as q
from tkinter import messagebox
from PIL import ImageTk, Image
import PIL.Image
w=Tk()
w.title("QR Code Generator")
w.iconbitmap("download.ico")
w.maxsize(width=600,height=600)
w.minsize(width=600,height=600)
def done():
    n=name.get()
    m=mob.get()
    ag=age.get()
    c=city.get()
    if n=="":
        messagebox.showerror("Error","Enter Name")
    elif m=="":
        messagebox.showerror("Error","Enter Mobile.no")
    elif ag=="":
        messagebox.showerror("Error","Enter Age")
    elif c=="":
        messagebox.showerror("Error","Enter City")
    else:
        messagebox.showinfo("Done","Successfull") 
        i=q.make("Name-: "+n+'\n'+"Mob.no-: "+m+'\n'+"Age-: "+ag+'\n'+"City-: "+c)
        i.save(n+".png")
        w.destroy()
        a=Tk()
        a.title("QR Code Generator")
        a.iconbitmap("download.ico")
        a.maxsize(width=600,height=600)
        a.minsize(width=600,height=600)
        photo=PhotoImage(file=n+".png")
        t=Label(image=photo).place(x=120,y=80)
        a.mainloop()
name=StringVar()
mob=StringVar()
age=StringVar()
city=StringVar()
l=Label(w,text="QR Code Generator",font=("MV Boli",36)).pack()
l1=Label(w,text="Name-:",font=("MV Boli",22)).place(x=130,y=200)
l2=Label(w,text="Mobile.no-:",font=("MV Boli",22)).place(x=130,y=270)
l3=Label(w,text="Age-:",font=("MV Boli",22)).place(x=130,y=340)
l4=Label(w,text="City-:",font=("MV Boli",22)).place(x=130,y=420)
e=Entry(w,bd=4,font=("MV Boli",12),textvariable=name).place(x=300,y=210)
e1=Entry(w,bd=4,font=("MV Boli",12),textvariable=mob).place(x=300,y=280)
e2=Entry(w,bd=4,font=("MV Boli",12),textvariable=age).place(x=300,y=350)
e3=Entry(w,bd=4,font=("MV Boli",12),textvariable=city).place(x=300,y=430)
b=Button(w,text="Generate",bd=4,font=("MV Boli",12),command=done).place(x=370,y=500)
w.mainloop()
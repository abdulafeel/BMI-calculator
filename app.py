from tkinter import *
root=Tk()
root.title("BMI CALCULATOR")

def bmicalculator():
    weight=float(w.get())
    height=float(h.get())
    bmi= round(weight/height**2,2)
    b.set(bmi)


frame=Frame(root)
frame.grid(column=1,row=3)

w=StringVar()
h=StringVar()
b=StringVar()



Label(frame,text="WEIGHT",font=20,fg="#1c1c1c").grid(column=0,row=0)
Entry(frame,textvariable=w,font=20,bg="#cdccd9",width=30).grid(column=1,row=0)

Label(frame,text="HEIGHT",font=20,fg="#1c1c1c").grid(column=0,row=1)
Entry(frame,textvariable=h,font=20,bg="#cdccd9",width=30).grid(column=1,row=1)


Label(frame,text="BMI=",font=20,fg="#1c1c1c").grid(column=0,row=2)
Label(frame,textvariable=b,font=20,fg="black",width=30).grid(column=1,row=2)

Button(frame,text="Calculate",command=bmicalculator,font=20,bg="#7ead47",fg="black",width=30).grid(column=1,row=3)




root.mainloop()

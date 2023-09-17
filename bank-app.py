import tkinter as tk
root=tk.Tk()
l1=tk.Label(root,text="user name")
l2=tk.Label(root,text="account number")
l3=tk.Label(root,text="balance")


t1=tk.Entry()
t2=tk.Entry()
t3=tk.Entry()

b1=tk.Button(text="registration")
b2=tk.Button(text="balance")
b3=tk.Button(text="deposit")



l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)

t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)

b1.grid(row=3,column=1)
b2.grid(row=4,column=1)
b3.grid(row=5,column=1)

tk.mainloop()
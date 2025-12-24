from tkinter import *
from tkinter.font import Font



root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Tkinter to do list')
V1 = StringVar()


count = 0

def enter():
    global count
    count += 1
    V0 = E1.get()
    L1.insert(END,f'{count}. {V0}')
    V1.set('')

def delete():
    del_task = L1.curselection()[0]
    L1.delete(del_task)

def clear():
    L1.delete(0,END)







Title = Label(root,text='Your to do list',font=('forte',20),fg='white')
Title.place(x=20,y=10)
E1 = Entry(root,width=15,textvariable=V1,font=('century gothic', 20))
E1.place(x = 40, y = 50)
B1 = Button(root, text='Enter',font=('cascadia mono',12),relief='ridge',bg='grey',command=enter)
B1.place(x = 300, y = 50)
B2 = Button(root, text='Clear',font=('cascadia mono',10),relief='ridge',bg='white',width=6,command=clear)
B2.place(x = 300, y = 340)
B3 = Button(root, text='Delete',font=('cascadia mono',10),relief='ridge',bg='coral',width=6,command=delete)
B3.place(x = 300, y = 300)

L1 = Listbox(root,width=33,height=15,font=('consolas',10))
L1.place(x = 40,y = 120)






root.mainloop()
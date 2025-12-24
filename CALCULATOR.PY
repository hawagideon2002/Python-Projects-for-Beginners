
# global variable works pretty much the same as any other variable,
# ie, for you to use it, you must first assign it before it can be used,
# you cannot use it before it is assigned





from tkinter import *


root = Tk()
root.title('Say hello to my tkinter Calculator')
root.geometry('300x350')
root.resizable(0,0)

v1 = StringVar()

string = ''


def button(clicked_button):
    global newstring
    global string
    entry_field = v1.get()
    E1.insert(END,clicked_button)

    if '+' or '*' or '-' or '/'in entry_field:

        string += str(clicked_button)
        newstring = string
        #print(newstring) This keeps track of the second string after any operator


def clear():
    v1.set('')

def back():
    entry_field = v1.get()
    last_int = (entry_field[:-1])
    v1.set(last_int)


def subtraction():
    global string
    global get1

    string = ''
    get1 = v1.get()
    E1.insert(END,'-')# this part implies that you should first get the first input and then insert the operator to avoid unnecessary concatinations that int or float can't calculate.


def addition():
    global string
    global get2

    string = ''
    get2 = v1.get()
    E1.insert(END,'+')


def multiplication():
    global string
    global get3

    string = ''
    get3 = v1.get()
    E1.insert(END,'x')



def division():
    global string
    global get4
    string = ''

    get4 = v1.get()
    E1.insert(END,'/')

def percentage():
    get5 = v1.get()
    percentage_value = float(get5)/100
    v1.set(round(percentage_value,2))




def solve():
    entry_field = E1.get()

    if '+' in entry_field:
        overall=float(get2) + float(newstring)
        v1.set(round(overall,10))

    elif 'x' in entry_field:
        overall=float(get3) * float(newstring)
        v1.set(round(overall,10))

    elif '/' in entry_field:
        overall=float(get4) / float(newstring)
        v1.set(round(overall,10))

    elif '-' in entry_field:
        overall = float(get1) - float(newstring)
        v1.set(round(overall,10))




E1 = Entry(root, textvariable=v1, font=('rockwell condensed',20,'bold') ,width=21)
E1.place(x=20,y=20)
label = Label(root,text='Tk calculator No eval',font=('arial bold',15),fg='white')
label.place(x = 20,y=60)
B1 = Button(root, text='1',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(1),bg='white',fg='black')
B1.place(x=20,y=100)
B2 = Button(root, text='2',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(2),bg='white',fg='black')
B2.place(x=61,y=100)
B3 = Button(root, text='3',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(3),bg='white',fg='black')
B3.place(x=102,y=100)
B4 = Button(root, text='4',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(4),bg='white',fg='black')
B4.place(x=20,y=138)
B5 = Button(root, text='5',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(5),bg='white',fg='black')
B5.place(x=61,y=138)
B6 = Button(root, text='6',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(6),bg='white',fg='black')
B6.place(x=102,y=138)
B7 = Button(root, text='7',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(7),bg='white',fg='black')
B7.place(x=20,y=176)
B8 = Button(root, text='8',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(8),bg='white',fg='black')
B8.place(x=61,y=176)
B9 = Button(root, text='9',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(9),bg='white',fg='black')
B9.place(x=102,y=176)
point = Button(root, text='.',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button('.'),bg='white',fg='black')
point.place(x=20,y=214)
B0 = Button(root, text='0',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=lambda:button(0),bg='white',fg='black')
B0.place(x=61,y=214)

percent = Button(root, text='%',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=percentage,bg='white',fg='black')
percent.place(x=102,y=214)
add = Button(root, text='+',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=addition,bg='white',fg='black')
add.place(x=191,y=100)
minus = Button(root, text='x',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=multiplication,bg='white',fg='black')
minus.place(x=232,y=100)
multiply = Button(root, text='-',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=subtraction,bg='white',fg='black')
multiply.place(x=232,y=138)
divide = Button(root, text='/',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=division,bg='white',fg='black')
divide.place(x=191,y=138)
equals = Button(root, text='=',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=solve,bg='white',fg='black')
equals.place(x=102,y=253)
clear = Button(root, text='C',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=clear,bg='coral',fg='black')
clear.place(x=61,y=253)
back_trace = Button(root, text='<-',font=('berlin sans fb',15,),width=3,height=1,relief='ridge',command=back,bg='white',fg='grey')
back_trace.place(x=20,y=253)

root.mainloop()
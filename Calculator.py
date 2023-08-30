from tkinter import *
from tkinter import font

def click(element):
    global op
    op=op+str(element)
    entry_text.set(op)

def evaluate():
    global op
    try:
        answer=str(eval(op))
        entry_text.set(answer)
    except:
        op='Error'
        entry_text.set(op)

def clear():
    global op
    op=""
    entry_text.set(op)

def delete():
    global op
    op=op[:-1]
    entry_text.set(op)

cal = Tk()
cal.title("Calculator")
cal['bg']='azure3'
op=""
cal.resizable(0,0)

entry_text= StringVar()
entry = Entry(width=12,font=('Times',34,'bold'),bd=12,bg='beige',justify='right',relief=GROOVE,textvariable=entry_text).grid(columnspan=4)

btn_exit= Button(text='EXIT',font=('Courier 15 bold'),bd=7,command=lambda:cal.destroy(),relief=GROOVE,activebackground='azure3',bg='beige',padx=75,pady=8).grid(row=1,columnspan=3)

btn_del= Button(text='DEL',font=('Courier 15 bold'),bd=7,command=delete,relief=GROOVE,bg='beige',activebackground='azure3',padx=10,pady=8).grid(row=1,column=3,pady=3)

bt7= Button(text='7',font=('Symbol 15 bold'),bd=7,command=lambda:click(7),relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=2,column=0)

bt8= Button(text='8',font=('Symbol 15 bold'),command=lambda:click(8),relief=GROOVE,bg='beige',activebackground='azure3',bd=7,padx=15,pady=8).grid(row=2,column=1)

bt9= Button(text='9',font=('Symbol 15 bold'),command=lambda:click(9),relief=GROOVE,bg='beige',activebackground='azure3',bd=7,padx=15,pady=8).grid(row=2,column=2)

btn_add= Button(text='+',font=('Times 15 bold'),command=lambda:click('+'),bd=7,relief=GROOVE,activebackground='azure3',bg='beige',padx=19,pady=8).grid(row=2,column=3)

bt6= Button(text='6',font=('Symbol 15 bold'),bd=7,command=lambda:click(6),relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=3,column=0)

bt5= Button(text='5',font=('Symbol 15 bold'),command=lambda:click(5),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=3,column=1)

bt4= Button(text='4',font=('Symbol 15 bold'),command=lambda:click(4),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=3,column=2)

btn_sub= Button(text='-',font=('Times 15 bold'),command=lambda:click('-'),relief=GROOVE,bg='beige',activebackground='azure3',bd=7,padx=20,pady=8).grid(row=3,column=3)

bt3= Button(text='3',font=('Symbol 15 bold'),bd=7,command=lambda:click(3),relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=4,column=0)

bt2= Button(text='2',font=('Symbol 15 bold'),command=lambda:click(2),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=4,column=1)

bt1= Button(text='1',font=('Symbol 15 bold'),command=lambda:click(1),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=4,column=2)

btn_mul= Button(text='*',font=('Times 15 bold'),command=lambda:click('*'),relief=GROOVE,bg='beige',activebackground='azure3',bd=7,padx=19,pady=8).grid(row=4,column=3)

bt0= Button(text='0',font=('Symbol 15 bold'),bd=7,command=lambda:click(0),relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=5,column=0)
 
btn_clear= Button(text='C',font=('Times 15 bold '),command=lambda:clear(),relief=GROOVE,bg='beige',activebackground='azure3',bd=7,padx=15,pady=8).grid(row=5,column=1)

btn_eval= Button(text='=',font=('Symbol 15 bold'),command=lambda:evaluate(),bd=7,relief=GROOVE,activebackground='azure3',bg='beige',padx=15,pady=8).grid(row=5,column=2)

btn_div= Button(text='/',font=('Times 15 bold'),command=lambda:click('/'),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=20,pady=8).grid(row=5,column=3)

bt_brack1= Button(text='(',font=('Symbol 15 bold'),bd=7,command=lambda:click('('),relief=GROOVE,bg='beige',activebackground='azure3',padx=15,pady=8).grid(row=6,column=0)
 
btn_brack2= Button(text=')',font=('Symbol 15 bold '),command=lambda:click(')'),relief=GROOVE,bg='beige',activebackground='azure3',bd=7,padx=15,pady=8).grid(row=6,column=1)

btn_dot= Button(text='.',font=('Symbol 15 bold'),command=lambda:click('.'),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=18,pady=8).grid(row=6,column=2)

btn_mod= Button(text='%',font=('Times 15 bold'),command=lambda:click('%'),bd=7,relief=GROOVE,bg='beige',activebackground='azure3',padx=13,pady=8).grid(row=6,column=3)

font.families()

cal.mainloop()

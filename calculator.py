from tkinter import *

expression = ""

def press(num):

    global expression
 

    expression = expression + str(num)
 

    equation.set(expression)
 
def equalpress():

    try:
 
        global expression
 

        total = str(eval(expression))
 
        equation.set(total)
 

        expression = ""
 

    except:
 
        equation.set(" error ")
        expression = ""
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":

    rea = Tk()
 

    rea.configure(background="grey")
 

    rea.title("Simple Calculator")
 

    rea.geometry("312x324")
 

    equation = StringVar()
 

    expression_field = Entry(rea, textvariable=equation)
 

    expression_field.grid(columnspan=40, ipadx=70)
 

    b1 = Button(rea, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), height=1, width=7)
    b1.grid(row=2, column=0)
 
    b2 = Button(rea, text=' 2 ', fg='black', bg='white',
                    command=lambda: press(2), height=1, width=7)
    b2.grid(row=2, column=1)
 
    b3 = Button(rea, text=' 3 ', fg='black', bg='white',
                    command=lambda: press(3), height=1, width=7)
    b3.grid(row=2, column=2)
 
    b4 = Button(rea, text=' 4 ', fg='black', bg='white',
                    command=lambda: press(4), height=1, width=7)
    b4.grid(row=3, column=0)
 
    b5 = Button(rea, text=' 5 ', fg='black', bg='white',
                    command=lambda: press(5), height=1, width=7)
    b5.grid(row=3, column=1)
 
    b6 = Button(rea, text=' 6 ', fg='black', bg='white',
                    command=lambda: press(6), height=1, width=7)
    b6.grid(row=3, column=2)
 
    b7 = Button(rea, text=' 7 ', fg='black', bg='white',
                    command=lambda: press(7), height=1, width=7)
    b7.grid(row=4, column=0)
 
    b8 = Button(rea, text=' 8 ', fg='black', bg='white',
                    command=lambda: press(8), height=1, width=7)
    b8.grid(row=4, column=1)
 
    b9 = Button(rea, text=' 9 ', fg='black', bg='white',
                    command=lambda: press(9), height=1, width=7)
    b9.grid(row=4, column=2)
 
    b0 = Button(rea, text=' 0 ', fg='black', bg='white',
                    command=lambda: press(0), height=1, width=7)
    b0.grid(row=5, column=0)
 
    plus = Button(rea, text=' + ', fg='black', bg='white',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(rea, text=' - ', fg='black', bg='white',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(rea, text=' * ', fg='black', bg='white',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(rea, text=' / ', fg='black', bg='white',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(rea, text=' = ', fg='black', bg='white',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(rea, text='Clear', fg='black', bg='white',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(rea, text='.', fg='black', bg='white',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)

    rea.mainloop()
    
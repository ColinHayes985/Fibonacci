# First class without the book
from  math import *
from graphics import *
from tkinter import simpledialog
from tkinter.ttk import Label
import tkinter as tk
def fibonacci():
    #Prompt user for length
    length = simpledialog.askinteger("Fibonacci Length", "How many numbers would you like in the sequence?")

    #Make neccesary variables and print
    x = 0
    y = 1
    fib = 0
    sequence=[]
    sequence.append(x)
    sequence.append(y)


    #Calculate and print numbers in sequence
    for i in range(length - 3):
        fib = x+y
        sequence.append(fib)
        x = y
        y = fib

    #Final calculation
    fib = x + y
    sequence.append(fib)
    output=""


    #Formatting output
    for i in range(sequence.__len__()-1):
        output=output+str(sequence[i])
        output=output+", "
    output=output+str(sequence[sequence.__len__()-1])
    output=output+"\n"+"The "+str(length)+"th "+"number in the fibonacci sequence is "+str(fib)

    #Print output to label
    root = tk.Tk()
    root.title("Fibonacci Sequence")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    label = Label(root, text=output)
    label.pack()

    root.mainloop()


fibonacci();
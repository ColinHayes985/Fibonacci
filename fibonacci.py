# TODO: Find out why graphics import is considered unused when statement removal causes errors
from graphics import *
from tkinter import simpledialog
from tkinter.ttk import Label
import tkinter as tk


def fibonacci():

    # Prompt user for length
    length = simpledialog.askinteger("Fibonacci Length", "How many numbers would you like in the sequence?")

    # Make necessary variables and print
    x = 0
    y = 1
    # TODO: Find out why fib is considered unused
    fib = 0
    sequence = [x, y]

    # Calculate and print numbers in sequence
    for i in range(length - 3):
        fib = x + y
        sequence.append(fib)
        x = y
        y = fib

    # Final calculation
    fib = x + y
    sequence.append(fib)
    output = ""

    # Formatting output (looks a little overly complicated, the purpose was to remove the final comma)
    # TODO: Work on inputs numbers ending in 1, 2, or 3 (display ...1st, ...2nd, or ...3rd instead of ...th
    #       when appropriate)
    for i in range(sequence.__len__()-1):
        output = output + str(sequence[i])
        output = output + ", "
    output = output + str(sequence[sequence.__len__() - 1])
    output = output + "\n" + "The " + str(length) + "th " + "number in the fibonacci sequence is: " + str(fib)

    # Print output to label
    # TODO: Figure out a way to make it work with large numbers (label cuts off text at end of window)
    # TODO: Figure out how to make the program end when output window is closed
    # Sequence fits window until length=40, end value will get cutoff when large enough
    root = tk.Tk()
    root.title("Fibonacci Sequence")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    label = Label(root, text=output)
    label.pack()

    root.mainloop()


fibonacci()

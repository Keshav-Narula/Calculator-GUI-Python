from tkinter import *

#Gets passed the character of the corresponding button that was pressed and adds it to the existing string representing the equation, 
# then displays the new equation onto the label
def add_to_equation_event(newChar):
    global equationStr
    equationStr += str(newChar)
    equationLabel.set(equationStr)

#Clears label display and the string value of the current equation stored
def clear_event():
    global equationStr
    equationLabel.set("")
    equationStr = ""

#Tries to use the python eval() operator, to evaluate the equation string, setting the result as a string to that variable before setting in onto the label
# To avoid breaking from arthimetic errors, Catches and specifies errors that could be raised zero division error and syntax error, 
# Security Issue eval() function not only evaluates calculations it can also evaluate python code, user could possibly inject code into program
def equals_event():
    global equationStr

    try:
        equationStr = str(eval(equationStr))

        equationLabel.set(equationStr)

    except ZeroDivisionError:
        clear_event()
        equationLabel.set("Zero Division Error")

    except SyntaxError:
        clear_event()
        equationLabel.set("Syntax Error")

window = Tk() #Create Instance of window

#GUI
window.geometry("325x275")
window.title("Calculator")

equationStr = ""

equationLabel = StringVar()
textResultLabel = Label(window, textvariable= equationLabel, font=("Arial", 20), height=2, width = 20, bg="white")
textResultLabel.grid(columnspan=5)


# Possible TODO: Put button instantiation into for loop
button1 = Button(window, text="1", command=lambda: add_to_equation_event(1), width = 5, font=14)
button1.grid(row=2,column=1)

button2 = Button(window, text="2", command=lambda: add_to_equation_event(2), width = 5, font=14)
button2.grid(row=2,column=2)

button3 = Button(window, text="3", command=lambda: add_to_equation_event(3), width = 5, font=14)
button3.grid(row=2,column=3)

button4 = Button(window, text="4", command=lambda: add_to_equation_event(4), width = 5, font=14)
button4.grid(row=3,column=1)

button5 = Button(window, text="5", command=lambda: add_to_equation_event(5), width = 5, font=14)
button5.grid(row=3,column=2)

button6 = Button(window, text="6", command=lambda: add_to_equation_event(6), width = 5, font=14)
button6.grid(row=3,column=3)

button7 = Button(window, text="7", command=lambda: add_to_equation_event(7), width = 5, font=14)
button7.grid(row=4,column=1)

button8 = Button(window, text="8", command=lambda: add_to_equation_event(8), width = 5, font=14)
button8.grid(row=4,column=2)

button9 = Button(window, text="9", command=lambda: add_to_equation_event(9), width = 5, font=14)
button9.grid(row=4,column=3)

button0 = Button(window, text="0", command=lambda: add_to_equation_event(0), width = 5, font=14)
button0.grid(row=5,column=2)

buttonPlus = Button(window, text="+", command=lambda: add_to_equation_event("+"), width = 5, font=14)
buttonPlus.grid(row=2,column=4)

buttonSubtract = Button(window, text="-", command=lambda: add_to_equation_event("-"), width = 5, font=14)
buttonSubtract.grid(row=3,column=4)

buttonMultiply = Button(window, text="*", command=lambda: add_to_equation_event("*"), width = 5, font=14)
buttonMultiply.grid(row=4,column=4)

buttonDivision = Button(window, text="/", command=lambda: add_to_equation_event("/"), width = 5, font=14)
buttonDivision.grid(row=5,column=4)

buttonOpenBracket = Button(window, text="(", command=lambda: add_to_equation_event("("), width = 5, font=14)
buttonOpenBracket.grid(row=5,column=1)

buttonCloseBracket = Button(window, text=")", command=lambda: add_to_equation_event(")"), width = 5, font=14)
buttonCloseBracket.grid(row=5,column=3)

buttonEquals = Button(window, text="=", command= equals_event, width = 11, font=14)
buttonEquals.grid(row=6,column=3, columnspan=2)

buttonClear = Button(window, text="Clear", command=clear_event, width = 6, font=14)
buttonClear.grid(row=6,column=1)

buttonDecimal = Button(window, text=".", command=lambda: add_to_equation_event("."), width = 5, font=14)
buttonDecimal.grid(row=6,column=2)

window.mainloop() #Endpoint, run mainloop

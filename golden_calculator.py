from tkinter import *


# METHODS
# ---------------------------------------------
def button_press(num):
    """
    display numbers and symbols when pressed
    :param num: button pressed
    :return: None
    """
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    """
    trigger = equals button
    calculate the result using eval function
    by handling some exceptions
    :return: None
    """
    global equation_text  # making equation text global
    try:
        total = str(eval(equation_text))  # EVAL :|
        equation_label.set(total)
        equation_text = total  # so we can reuse the equals
    except ZeroDivisionError:
        equation_label.set("/ by '0' is forbidden")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""


def clear():
    """
    trigger = AC button
    clear the display
    :return: None
    """
    global equation_text

    equation_label.set("")
    equation_text = ""


# END METHODS
# ---------------------------------------------

# MAIN WINDOW
# ============================================================================
window = Tk()
window.title("Golden Calculator")
window.config(bg="Black")
window.resizable(False, False)  # non-resizable

equation_text = ""
equation_label = StringVar()

display = Label(window, font=("consoles", 20, "bold"), bg="#FFCE30", width=19, height=1, textvariable=equation_label,
                relief=RAISED, bd=3, pady=7, )
display.pack(pady=3)

frame = Frame(window, relief=RAISED, bd=8)
frame.pack()

# I Actually tried all these buttons using 2 for loops and a list contains text
# it works on the UI(text,grid row,col) part but not in command part in buttons
Button(frame, text=7, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="#400080", height=2, width=4, command=lambda: button_press(7)).grid(row=1, column=0)
Button(frame, text=8, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="#400080", height=2, width=4, command=lambda: button_press(8)).grid(row=1, column=1)
Button(frame, text=9, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="#400080", height=2, width=4, command=lambda: button_press(9)).grid(row=1, column=2)
Button(frame, text="AC", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="red", height=2, width=4, command=clear).grid(row=1, column=3)

Button(frame, text=4, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="green", height=2, width=4, command=lambda: button_press(4)).grid(row=2, column=0)
Button(frame, text=5, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="green", height=2, width=4, command=lambda: button_press(5)).grid(row=2, column=1)
Button(frame, text=6, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="green", height=2, width=4, command=lambda: button_press(6)).grid(row=2, column=2)
Button(frame, text="+", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="#400080", height=2, width=4, command=lambda: button_press('+')).grid(row=2, column=3)

Button(frame, text=1, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="Yellow", height=2, width=4, command=lambda: button_press(1)).grid(row=3, column=0)
Button(frame, text=2, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="Yellow", height=2, width=4, command=lambda: button_press(2)).grid(row=3, column=1)
Button(frame, text=3, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="Yellow", height=2, width=4, command=lambda: button_press(3)).grid(row=3, column=2)
Button(frame, text="-", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="green", height=2, width=4, command=lambda: button_press("-")).grid(row=3, column=3)

Button(frame, text="0", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="red", height=2, width=4, command=lambda: button_press(0)).grid(row=4, column=0)
Button(frame, text="*", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="Yellow", height=2, width=4, command=lambda: button_press('*')).grid(row=4, column=1)
Button(frame, text="/", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="red", height=2, width=4, command=lambda: button_press("/")).grid(row=4, column=2)
Button(frame, text="=", font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="#FFD700",
       activeforeground="red", height=2, width=4, command=equals).grid(row=4, column=3)

window.mainloop()

# END MAIN WINDOW
# ============================================================================

#JMJ
# @author: Martin Tejada
# @date: March 11, 2025
# @description: Simple Calculator in python

from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Dodo Calculator")
window.geometry("400x600")
window.config(bg='#257887')

# Custom Image (pixel art) of dodo bird
dodo = Image.open("dodolistt.png")
rdodo = dodo.resize((305, 100))

# Converting to PhotoImage so I can put it into the label, since PhotoImage does not have a resize function and cannot be used in a Label
r_dodo = ImageTk.PhotoImage(rdodo)

# If any button other than "=" or "clr" is pressed
def update_label(value):
    a = screen.cget("text") # get the value in the screen
    a += value              # add the value of the button (text on button)
    screen.config(text=a)   # add the concatenated value to the screen

def compute():
    try:
        a = eval(screen.cget("text")) # get value from the screen and compute
        screen.config(text=str(a)) # change back to string so I can add more values, since I can't add string to Integers
    except ZeroDivisionError:
        screen.config(text="Error: Division by 0") # handle division by 0
    except (ArithmeticError, Exception) as e: # handle arithmetic errors
        screen.config(text="Error: " + str(e))

def clear():
    screen.config(text="") # set text to "" 

frame  = Frame(window)   # frame to hold buttons and grid
frame.config(bg='#8CD19C') 

screen = Label(window, text="", font=("Plaza", 20), fg='white', image=r_dodo, compound="center") # screen to display user input and calculations

def create_button(text, row, col, command=None): # function to create buttons @param text: the text on the button, @param row/col = row and coloumn value, @param command: the command for the button
    button =  Button(frame, text=text, padx=25, pady=20, bg='#E4BB97', command=command)
    button.grid(row=row, column=col, padx=5, pady=5)
    return button

buttons = [ # list that holds button text and row and coloumn data
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 0, 3), ('-', 1, 3),
    ('*', 2, 3), ('/', 3, 3), ('=', 4, 3),
    ('clr', 0, 0)
]

# Add number buttons and operations
for (text, row, col) in buttons:
    if text == '=':
        create_button(text, row, col, command=compute)
    elif text == 'clr':
        create_button(text, row, col, command=clear)
    else:
        create_button(text, row, col, command=lambda num=text: update_label(num))

screen.place(x=50,y=50)
frame.place(x=50,y=200)

window.mainloop()
#JMJ
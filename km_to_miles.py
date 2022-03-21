from tkinter import *

# Create an empty Tkinter window:
window = Tk()

def km_to_miles():
    # Get user value from input box and multiply by 1.6 to get miles
    miles = float(e1_value.get())*1.6
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)
    t1.insert(END, miles)

# The km_to_miles() function is called when the button is pushed
b1 = Button(window, text = 'Execute', command = km_to_miles)
b1.grid(row = 0, column = 0)

e1_value = StringVar()  # Create a special StringVar object
e1 = Entry(window, textvariable = e1_value)  # Create an Entry box for users to enter the value
e1.grid(row = 0, column = 1)

# Create the empty text boxes t1:
t1 = Text(window, height =1, width=20)
t1.grid(row=0, column = 2)

# This makes sure to keep the main window open
window.mainloop()

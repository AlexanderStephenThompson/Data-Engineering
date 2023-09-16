from tkinter import *

root = Tk()

entry = Entry(root)
entry.pack()
entry.insert(0,"Enter your name") # Default text

def clickAction():
    greeting = f"Hello there, {entry.get()}"

    # Insert Label
    myLabel = Label(root, text = greeting)
    myLabel.pack()

myButton = Button(root, text = "Submit", command=clickAction, fg="blue")
myButton.pack()



root.mainloop()
from tkinter import *
import tkinter
from tkinter import ttk

""" Very Useful resources
    •	https://likegeeks.com/python-gui-examples-tkinter-tutorial/ 
    •	https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/tkinter-overview ***
    •	https://www.datacamp.com/community/tutorials/gui-tkinter-python
    •	https://www.geeksforgeeks.org/python-gui-tkinter/
    •	https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
    •	https://tkdocs.com/tutorial/
    •	https://www.geeksforgeeks.org/python-tkinter-tutorial/
    •	https://stackabuse.com/python-gui-development-with-tkinter/ 
"""

root = tkinter.Tk()
root.title("Kelston University App") 
root.geometry('400x450') # Default window size
logo = PhotoImage(file = "Kelston.png") 
root.iconphoto(False, logo) 


# text = Text(root)
# myFont = font(family="Times New Roman", size=12)
# text.configure(font=myFont)

# Menu
def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")

# Widgets
# root.widgetName(parentContainerName, other attributes)
# Example_Widget = someWidget(parentContainer,
#                         text= "This is a test",
#                         bg="yellow",
#                         fg="blue",
#                         font=("Courier", 16, "italic"),
#                         justify (left, right, center),
#                         command = functionName, # Note the lack of ()
#                         state = ['disabled'] or ['!disabled']
#                          )

# someWidget.config(Arugment = Whatever) # Allows you to add or adjust attributes of a widget


# Top Menu
root.option_add('*tearOff', False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

file.add_command(label = 'New', command = lambda: print('New File'))
file.add_separator()
file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
file.add_command(label = 'Save', command = lambda: print('Saving File...'))

file.entryconfig('New', accelerator = 'Ctrl+N')
logo = PhotoImage(file = 'python_logo.gif').subsample(10, 10) # Change path as needed
file.entryconfig('Open...', image = logo, compound = 'left')
file.entryconfig('Open...', state = 'disabled')

file.delete('Save')
save = Menu(file)
file.add_cascade(menu = save, label = 'Save')
save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
save.add_command(label = 'Save All', command = lambda: print('Saving All...'))

# Layout (Geometry manager)
#Pack

#Grid

#Place


# Styling
# Colors, border width, 

# Buttons
# button = ttk.Button(root, text = "Text!")
# button.pack()
infoButton = Button(root, text = "Info", bg="dodgerblue3", fg="cyan") #bg is background and fg is foreground
infoButton.pack()

warningButton = Button(root, text = "Warning", bg="darkorange2", fg="gold1")
warningButton.pack()

dangerButton = Button(root, text = "Danger", bg="red4", fg="tomato2")
dangerButton.pack()

# Label 
labelframe_widget = tkinter.LabelFrame(root, text="Breakfast Choice")
label_widget= tkinter.Label(labelframe_widget,text="Child widget of the LabelFrame")
labelframe_widget.pack(padx=10, pady=10)
label_widget.pack()


# Radio button
checkbutton = ttk.Checkbutton(root)
checkbutton.pack()


breakfastChoice = StringVar()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfastChoice, value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfastChoice, value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfastChoice, value = 'SPAM').pack()
print(breakfastChoice.get()) # Note: value will be empty if no selection is made

label_widget.config(textvariable = breakfastChoice)

# Check button
checkbutton_widget = tkinter.Checkbutton(root, text="Check button")
checkbutton_widget.pack()

# Combo box
month = StringVar()
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
combobox = ttk.Combobox(root, textvariable = month, values = months)
combobox.pack()

# Treeview
# Tree View

# Icons
logo = PhotoImage(file="Python.png").subsample(13,13)

# Columns
treeview = ttk.Treeview(root, columns=("Version"))
treeview.pack()

treeview.column("Version", width = 50, anchor = 'center')
treeview.heading("Version", text = "Version")


# Rows
treeview.insert("", '0', "item 1", text= "Branch 1")

treeview.insert("", '1', "item 2", text= "Branch 2")
treeview.insert("item 2", "end", "Python", text="Python", image = logo)
treeview.set('Python', 'Version', '3.9')

treeview.insert("", '2', "item 3", text= "Branch 3")

# Spinbox
year = StringVar()
Spinbox(root, from_=1990, to=2020, textvariable = year).pack()

# Entry Fields
entry = Entry(root)
entry.pack()

# Horizontal Scale
scale_widget = tkinter.Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL)
scale_widget.set(25)
scale_widget.pack()

# Verticle Scale
scale_widget = tkinter.Scale(root, from_=0, to=100, orient=tkinter.VERTICAL)
scale_widget.set(25)
scale_widget.pack()

# Progress Bar
value = DoubleVar()
progressBar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200, variable = value)
progressBar.pack()
progressBar.config(mode="determinate", maximum = 10000.0, value = 4.2)
# progressBar.step(1) # Increment with some calculation

# Scale
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_=0.0, to=10000.0)
scale.pack()

labelframe_widget = LabelFrame(root, text="Danger Level")
label_widget= Label(labelframe_widget, textvariable= value)
labelframe_widget.pack(padx=10, pady=10)
label_widget.pack()

# Structure
# root.resizable(False, False) #Enables resizing of the window or not.
# root.maxsize(640, 1000)
# root.minize(320, 500)

#Paned window
panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill=BOTH, expand = True)

frame1 = ttk.Frame(panedwindow,width=100, height = 200, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow,width=400, height = 200, relief = SUNKEN)

panedwindow.add(frame1, weight = 0)
panedwindow.add(frame2, weight = 2)

# Tabs
tabs = ttk.Notebook(root)
tabs.pack()

frame1 = ttk.Frame(tabs)
frame2 = ttk.Frame(tabs)

tabs.add(frame1, text = 'One')
tabs.add(frame2, text = 'Two')

ttk.Button(frame1, text = 'Click Me').pack()


#Label frames
frame = ttk.Frame(root, height = 100, width = 200, relief = RIDGE)
frame.pack(pady=10) # Adds some margin

ttk.Button(frame, text = 'Click Me', padding=(30,15)).pack()

labelFrame = LabelFrame(root, text="Label Frame")
labelFrame.pack(padx=10, pady=10)
label_widget= Label(labelFrame, height = 10, width = 20, text = 'My Frame')
label_widget.pack()


# Removing Elements
# widget.destroy()

root.mainloop() # You need this, at the end of your script, for the window to appear.



# ## Class form 
# # from tkinter import Tk, Label, Button

# # class MyFirstGUI:
# #     def init(self, master):
# #         self.master = master
# #         master.title("A simple GUI")


# #         self.label = Label(master, text="This is our first GUI!")
# #         self.label.pack()

# #         self.greet_button = Button(master, text="Greet", command=self.greet)
# #         self.greet_button.pack()

# #         self.close_button = Button(master, text="Close", command=master.quit)
# #         self.close_button.pack()

# #     def greet(self):
# #         print("Greetings!")

# # root = Tk()
# # my_gui = MyFirstGUI(root)
# # root.mainloop()
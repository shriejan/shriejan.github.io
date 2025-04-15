import tkinter as tk 

root = tk.Tk()

button = tk.Button(text='çute button')
button.pack()

checkButton = tk.Checkbutton(text='test checkbutton')
checkButton.pack()

entry = tk.Entry(textvariable='hello!')
entry.pack()

# list box
listbox = tk.Listbox()
listbox.pack()
listbox.insert(tk.END,'ápple')
listbox.insert(tk.END,'mango')

# Create a Menu bar
menubar = tk.Menu(root)

# Create a dropdow file
file_menu = tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Create a dropdowe edit
edit_menu = tk.Menu(menubar,tearoff=0)
edit_menu.add_command(label='édit window')
edit_menu.add_command(label='édit screen')
edit_menu.add_command(label='édit view')
edit_menu.add_command(label='édit font')
menubar.add_cascade(label="edit", menu=edit_menu)

selection_menu = tk.Menu(menubar)
selection_menu.add_command(label="Select All")
selection_menu.add_command(label="Expand Selection")
selection_menu.add_command(label="Shrink Selection")
menubar.add_cascade(label="selection", menu=selection_menu)


# Configure the root to display the menu
root.config(menu=menubar)


tk.mainloop()
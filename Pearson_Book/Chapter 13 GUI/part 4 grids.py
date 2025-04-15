import tkinter as tk 
root = tk.Tk()
root.title('Basic Grids')

screen = tk.Frame()
screen.pack(side='top')

skrn = tk.Entry(screen)
skrn.pack()

keypad = tk.Frame()
keypad.pack(side='bottom')


b1 = tk.Button(s=keypad,text='1')
b1.grid(row=0,column = 0)
b2 = tk.Button(s=keypad,text='2')
b2.grid(row=0,column = 1)
b3 = tk.Button(s=keypad,text='3')
b3.grid(row=0,column = 2)
b4 = tk.Button(s=keypad,text='4')
b4.grid(row=0,column = 3)


tk.mainloop()

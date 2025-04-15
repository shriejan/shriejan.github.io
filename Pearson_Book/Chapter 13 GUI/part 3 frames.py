import tkinter as tk 
root = tk.Tk()
root.title('Basic Frames')

frame1 = tk.Frame(root)
frame1.pack(side='left')


frame2 = tk.Frame(root)
frame2.pack(side='left')

frame3 = tk.Frame(root)
frame3.pack(side='bottom')

label1 = tk.Label(frame1,text='life is life')
label1.pack()

label2 = tk.Label(frame2,text='hello hi')
label2.pack()

label3 = tk.Label(frame3,text='My Name is')
label3.pack()

button1 = tk.Button(frame1,text='hello its me button')
button1.pack()

button2 = tk.Button(frame2,text='hello i am button 2')
button2.pack()

button3 = tk.Button(frame3,text='Shriejan')
button3.pack()

root.mainloop()

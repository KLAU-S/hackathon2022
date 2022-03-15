import tkinter as tk
from tkinter import *

root = tk.Tk()
def printData(firstName, lastName):
    print(firstName)
    print(lastName)
    root.destroy()

def get_input():

    firstName = entry1.get()
    lastName = entry2.get()
    printData(firstName, lastName)

#Label 1
label1 = Label(root,text = 'Percentage in OS')
label1.pack()
label1.config(justify = CENTER)
entry1 = Entry(root, width = 30)
entry1.pack()


label2 = Label(root, text='Percentage in Algorithms')
label2.pack()
label2.config(justify = CENTER)
entry2 = Entry(root, width = 30)
entry2.pack()

label3 = Label(root, text='Percentage in S/W')
label3.pack()
label3.config(justify = CENTER)
entry3 = Entry(root, width = 30)
entry3.pack()

label4 = Label(root, text='Percentage in CN')
label4.pack()
label4.config(justify = CENTER)
entry4 = Entry(root, width = 30)
entry4.pack()

label5 = Label(root, text='Percentage in Electronics')
label5.pack()
label5.config(justify = CENTER)
entry5 = Entry(root, width = 30)
entry5.pack()

label6 = Label(root, text='Percentage in COA')
label6.pack()
label6.config(justify = CENTER)
entry6 = Entry(root, width = 30)
entry6.pack()

label7 = Label(root, text='Percentage in S/W')
label7.pack()
label7.config(justify = CENTER)
entry7 = Entry(root, width = 30)
entry7.pack()


button1 = Button(root, text = 'submit')
button1.pack() 
button1.config(command = get_input)





canvas = tk.Canvas(root, height=720, width=1080, bg="white")
canvas.pack()
frame = tk.Frame(root, bg="black")
root.mainloop()
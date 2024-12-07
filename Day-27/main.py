from tkinter import *
my_window = Tk()
my_window.title("My First GUI Program")
my_window.minsize(width=500, height=300)
my_label = Label(text="I am a Label", font=("Arial", 24, "normal"))
my_label.grid(row=1, column=1)

def clicked():
    my_label.config(text = user_input.get())

button1 = Button(text = "Click me!!", command = clicked)
button1.grid(row=2, column=2)

button2 = Button(text = "Click me!!")
button2.grid(row=1, column=3)

user_input = Entry(width = 10)
user_input.grid(row=3, column=4)



my_window.mainloop()


import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

# Function to search in the wikipedia database
def answer():
    question = questionEntry.get()
    answer = wikipedia.summary(question)
    showinfo(" Answer", answer)

# Sets the root config
Root = Tk(className=" Wikipedia Search Tool")
Root.geometry("500x300")

# Sets the base canvas
Canvas = Canvas(Root, bg='Light Grey')
Canvas.place(relwidth=1.0, relheight=1.0)

#Sets the language and gets the text variable for the search in the Wikipedia DataBase
wikipedia.set_lang("pt")
question = StringVar()
questionEntry = Entry(Canvas,textvariable=question)
questionEntry.place(relx=.5, rely=.3, height=20, anchor=CENTER)

# Button to execute the search function
buttonSearch = Button(Canvas, command=answer, text='Search now', font='Arial 12 bold', fg='Red', bg='Light Grey', height=3)
buttonSearch.place(relx=.5, rely=.5, anchor=CENTER)

# Copyright  and "developed by" text
copyrightLabel = Label(Canvas, text='Vesion: (ALPHA) 0.2 Developed by Pedro S. (p-py) / All rights reserved ©', font='Arial  10 bold', bg='#ddd', fg='#555')
copyrightLabel.place(relx=.5, rely=.95, anchor=CENTER)


Root.mainloop()
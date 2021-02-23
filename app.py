import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

def answer():
    question = questionEntry.get()
    answer = wikipedia.summary(question)
    showinfo(" Answer", answer)

Root = Tk(className=" Wikipedia Search Tool")
Root.geometry("500x300")

Canvas = Canvas(Root, bg='Light Grey')
Canvas.place(relwidth=1.0, relheight=1.0)

wikipedia.set_lang("pt")
question = StringVar()
questionEntry = Entry(Canvas, textvariable=question)
questionEntry.place(relx=.5, rely=.3, anchor=CENTER)

buttonSearch = Button(Canvas, command=answer, text='Search now', fg='Red', bg='Light Grey')
buttonSearch.place(relx=.5, rely=.4, anchor=CENTER)

Root.mainloop()
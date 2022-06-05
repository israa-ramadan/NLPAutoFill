from tkinter import *
import tkinter as tk
from Assignment2_NLP import *


def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    test_list = Autofill(value)

    # get data from test_list
    if value == '':
        data = []
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)

                # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')


screen = tk.Tk()
test_list = []

inputVal = StringVar()
duckGo = PhotoImage(file="duckduckgo.png")
duckGo = duckGo.subsample(3, 3)
screen.config(height=700, width=700, bg="white")
screen.title("NLP form")

formHeading = Label(text="NLP Testing form", bg="#E37151", width="30", height="2",
                    font=("Times New Roman", 25, "bold"))
formInputLabel = Label(screen, image=duckGo, bg="white")

sentenceEntry = Entry(textvariable=inputVal, width=50)
sentenceEntry.bind('<KeyRelease>', on_keyrelease)

listbox = tk.Listbox(screen, width=40)

# listbox.bind('<Double-Button-1>', on_select)
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(test_list)

formHeading.pack()
formInputLabel.pack(pady=30)
sentenceEntry.pack(pady=10)
listbox.pack()

screen.mainloop()

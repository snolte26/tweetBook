import os
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk

import certifi
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('tweetBook')

messageDisplay = ttk.Label(root, text="", font=("Helvetica", 14))

text = tk.Text(root, wrap="none", bg='lightblue')
vsb = tk.Scrollbar(orient="vertical", command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
text.pack(fill="both", expand=True)


def messages():
    ConnectString = os.getenv('CONNECTION_STRING')
    cluster = MongoClient(ConnectString, tlsCAFile=certifi.where())
    db = cluster["socialMedia"]["messages"]
    all = db.find({}).sort([('date', pymongo.DESCENDING), ('time', pymongo.DESCENDING)])
    date = datetime.now().strftime("%x")

    for messages in all:
        try:
            if date == messages["date"]:
                b = tk.Label(
                    root,
                    text=str(f"Today - {messages['time']}"),
                    font=("Helvetica", 14),
                    fg='red',
                    bg='lightgray'
                )
                text.window_create("end", window=b)
                text.insert("end", "\n")

                # print(colored(f"Today - {messages['time']}", 'red'))
            else:
                b = tk.Label(
                    root,
                    text=str(f"{messages['date']} - {messages['time']}"),
                    font=("Helvetica", 14),
                    fg='red',
                    bg='lightgray'
                )
                text.window_create("end", window=b)
                text.insert("end", "\n")

                # print(colored(f"{messages['date']} - {messages['time']}", 'red'))
            b = tk.Label(
                root,
                text=str(f"Post ID: {messages['count']}"),
                font=("Helvetica", 12),
                fg='purple',
                bg='lightgray'
            )
            text.window_create("end", window=b)
            text.insert("end", "\n")

            # print(colored(f"Post ID: {messages['count']}", 'yellow'))
            b = tk.Label(
                root,
                text=str("From: " + messages['id']),
                font=("Helvetica", 12),
                fg='maroon',
                bg='lightgray'
            )
            text.window_create("end", window=b)
            text.insert("end", "\n")

            # print(colored("From: ", 'green'), messages['id'])
            b = tk.Label(
                root,
                text=str("Message: " + messages['message']),
                font=("Helvetica", 12),
                wraplength=300,
                fg='green',
                bg='lightgray'
            )
            text.window_create("end", window=b)
            text.insert("end", "\n")

            # print(colored("Message: ", 'green'), messages['message'])
            b = tk.Label(
                root,
                text=str("----------------------"),
                font=("Helvetica", 12),
                bg='lightgray'
            )
            text.window_create("end", window=b)
            text.insert("end", "\n")

            # print("----------------------")
        except:
            pass
    text.configure(state="disabled")


def new_message():
    message = msg.get()
    person = username.get()

    cluster = MongoClient(
        "Your Connection String Here", tlsCAFile=certifi.where())
    db = cluster["socialMedia"]["messages"]
    all = db.find({})
    date = datetime.now().strftime("%x")
    time = datetime.now().strftime("%X")
    count = db.count_documents({})

    newMessage = {"count": count + 1, "id": person, "message": message, "date": date, "time": time}
    db.insert_one(newMessage)

    msgSent.delete('1.0', END)
    msgSent.insert(INSERT, "Message Sent!")
    msgSent.update()


def refresh():

    root.destroy()
    os.startfile("tweetBookGUI.pyw")
    pass


def autoMod():
    cluster = MongoClient(
        "Your Connection String Here", tlsCAFile=certifi.where())
    db = cluster["socialMedia"]["messages"]
    all = db.find({})
    today = datetime.now()
    day = timedelta(days=30)
    lastMonth = today - day

    count = db.count_documents({})

    for messages in all:
        try:
            if lastMonth.strftime("%x") >= messages["date"]:
                db.delete_one(messages)
        except:
            pass

    pass


message_button = ttk.Button(
    root,
    text="New Message",
    command=lambda: new_message()
)
message_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
message_button.place(
    x=375,
    y=95
)

refresh_button = ttk.Button(
    root,
    text="Refresh",
    command=lambda: refresh()
)
refresh_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
refresh_button.place(
    x=375,
    y=165
)

username = tk.StringVar()
frameNAME = LabelFrame(root, text='Username')
frameNAME.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
frameNAME.place(
    x=350,
    y=10
)
Entry(frameNAME, textvariable=username).pack()
msg = tk.StringVar()
frameMSG = LabelFrame(root, text='Message')
frameMSG.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
frameMSG.place(
    x=350,
    y=50
)
Entry(frameMSG, textvariable=msg).pack()

msgSent = tk.Text(root, width=15, height=2)
msgSent.place(
    x=350,
    y=125
)

autoMod()
messages()

root.config(bg='lightblue')
root.mainloop()

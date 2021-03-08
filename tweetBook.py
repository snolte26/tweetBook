from pymongo import MongoClient
from datetime import datetime
from termcolor import colored
import time
import os


def socialMedia(userPass, username):
    while True:
        os.system('cls')
        quit = False

        cluster = MongoClient(
            "Your Connection String Here")
        db = cluster["socialMedia"]["messages"]
        all = db.find({})
        date = datetime.now().strftime("%x")

        for messages in all:
            try:
                if date == messages["date"]:
                    print(colored(f"Today - {messages['time']}", 'red'))
                else:
                    print(colored(f"{messages['date']} - {messages['time']}", 'red'))
                print(colored("From: ", 'green'), messages['id'])
                print(colored("Message: ", 'green'), messages['message'])
                print("----------------------")
            except:
                pass

        person = str(username)

        while True:
            print("Please Choose an option 1-2")
            print("1. New Message")
            print("2. Refresh Messages")
            print("3. Quit")
            choice = int(input("Choice: "))
            if choice > 0 and choice < 3:
                if choice == 1:
                    message = input("Messgae: ")

                    time = datetime.now().strftime("%X")

                    msg = {"id": person, "message": message, "date": date, "time": time}
                    db.insert_one(msg)
                else:
                    break
            elif choice == 3:
                quit = True
                break
        if quit:
            break


def fileExists():
    # tries to open this file
    # if successful, close it and return true
    # otherwise return false
    try:
        f = open("userPass.txt")
        f.close()
        return True
        # Do something with the file
    except IOError:
        print("No Login Found")
        return False


def setup():
    userPass = open("userPass.txt", "w+")
    print("Beginning initial setup")
    print()

    user = input("Enter Username: ") + "\n"
    passw = input("Enter Password: ") + "\n"

    userPass.writelines(user)
    userPass.writelines(passw)
    return (user.replace("\n", ""))


def login(userPass):
    attemptLimit = 3
    attempts = 0

    while True:
        for word in userPass:
            username = word.replace("\n", "")
            password = next(userPass).replace("\n", "")
            break
        user = input("Username: ")
        passw = input("Password: ")

        if username == user and password == passw:
            break
        else:
            attempts += 1
            print("Wrong Username or Password")

        if attempts >= attemptLimit:
            print("Too many wrong attempts")
            print("Please wait 2 minutes "
                  "before trying again")
            attempts = 0
            time.sleep(120)
    return (user)


def main():
    # check if username/password file exists
    exists = fileExists()
    if exists:
        userPass = open("userPass.txt", "r")
        username = login(userPass)
        socialMedia(userPass, username)
    else:
        username = setup()
        userPass = open("userPass.txt", "r")
        socialMedia(userPass, username)


main()

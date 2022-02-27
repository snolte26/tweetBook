import certifi
from pymongo import MongoClient
from datetime import datetime
from termcolor import colored
import time
import os, sys
from dotenv import load_dotenv
load_dotenv()

def socialMedia(username):
    quit = False

    while True:
        os.system("cls" if sys.platform == "win32" else "clear")

        print(colored(".___________.____    __    ____  _______  _______ .___________..______     ______     ______    __  ___ ", 'blue'))
        print(colored("|           |\   \  /  \  /   / |   ____||   ____||           ||   _  \   /  __  \   /  __  \  |  |/  / ", 'blue'))
        print(colored("`---|  |----` \   \/    \/   /  |  |__   |  |__   `---|  |----`|  |_)  | |  |  |  | |  |  |  | |  '  /  ", 'blue'))
        print(colored("    |  |       \            /   |   __|  |   __|      |  |     |   _  <  |  |  |  | |  |  |  | |    <   ", 'blue'))
        print(colored("    |  |        \    /\    /    |  |____ |  |____     |  |     |  |_)  | |  `--'  | |  `--'  | |  .  \  ", 'blue'))
        print(colored("    |__|         \__/  \__/     |_______||_______|    |__|     |______/   \______/   \______/  |__|\__\ ", 'blue'))
        print("")

        ConnectString = os.getenv('CONNECTION_STRING')
        cluster = MongoClient(ConnectString, tlsCAFile=certifi.where())

        """For those with a local database, use the following instead:"""
        # cluster = MongoClient('localhost', 27017)
        
        db = cluster["socialMedia"]["messages"]
        all = db.find({})
        date = datetime.now().strftime("%x")

        for messages in all:
            try:
                if date == messages["date"]:
                    print(colored(f"Today - {messages['time']}", 'red'))
                else:
                    print(colored(f"{messages['date']} - {messages['time']}", 'red'))
                print(colored(f"Post ID: {messages['count']}", 'yellow'))
                print(colored("From: ", 'green'), messages['id'])
                print(colored("Message: ", 'green'), messages['message'])
                print("----------------------")
            except:
                pass

        person = str(username)

        while True:
            print()
            print(colored(".___________..______  ", 'blue'))
            print(colored("|           ||   _  \  ", 'blue'))
            print(colored("`---|  |----`|  |_)  | ", 'blue'))
            print(colored("    |  |     |   _  <  ", 'blue'))
            print(colored("    |  |     |  |_)  | ", 'blue'))
            print(colored("    |__|     |______/  ", 'blue'))
            print()
            print("Please Choose an option 1-6")
            print("1. New Message")
            print("2. Refresh Messages")
            print("3. View Your Posts")
            print("4. Search Users")
            print("5. Delete Your Post")
            print("6. Quit")
            choice = int(input("Choice: "))

            if choice > 0 and choice < 6:

                # creates a message for the user to post
                if choice == 1:
                    count = db.count_documents({})
                    message = input("Messgae: ")

                    time = datetime.now().strftime("%X")

                    msg = {"count": count + 1, "id": person, "message": message, "date": date, "time": time}
                    db.insert_one(msg)

                # breaks out of nested loop
                elif choice == 2:
                    break

                # showing users posts
                elif choice == 3:
                    os.system('cls')
                    userPosts = db.find({'id': person})
                    for messages in userPosts:
                        try:
                            if date == messages["date"]:
                                print(colored(f"Today - {messages['time']}", 'red'))
                            else:
                                print(colored(f"{messages['date']} - {messages['time']}", 'red'))
                            print(colored(f"Post ID: {messages['count']}", 'yellow'))
                            print(colored("From: ", 'green'), messages['id'])
                            print(colored("Message: ", 'green'), messages['message'])
                            print("----------------------")
                        except:
                            pass

                # search for users
                elif choice == 4:
                    os.system('cls')
                    person = input("Enter Users Name: ")
                    userPosts = db.find({'id': person})
                    for messages in userPosts:
                        try:
                            if date == messages["date"]:
                                print(colored(f"Today - {messages['time']}", 'red'))
                            else:
                                print(colored(f"{messages['date']} - {messages['time']}", 'red'))
                            print(colored(f"Post ID: {messages['count']}", 'yellow'))
                            print(colored("From: ", 'green'), messages['id'])
                            print(colored("Message: ", 'green'), messages['message'])
                            print("----------------------")
                        except:
                            pass
                # delete your own posts
                elif choice == 5:
                    persona = str(username)
                    postDelete = int(input("Post ID to Delete: "))
                    query = db.find_one({"count": postDelete, "id": persona})
                    try:
                        db.delete_one(query)
                    except:
                        pass

            # close the program
            elif choice == 6:
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

        directory = os.path.dirname(os.path.abspath(__file__))
        # command = directory + "\\tweetBook_AutoMod.py"
        command = os.path.join(directory, 'tweetBook_AutoMod.py')
        os.system(command)

        socialMedia(username)
    else:
        username = setup()
        userPass = open("userPass.txt", "r")

        directory = os.path.dirname(os.path.abspath(__file__))
        command = directory + "\\tweetBook_AutoMod.py"
        os.system(command)

        socialMedia(username)


main()

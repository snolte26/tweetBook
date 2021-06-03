import certifi
import discord
from pymongo import MongoClient
from datetime import datetime

client = discord.Client()
keywords = ["tweetBookAdd", "tweetBookRefresh", "%help"]


@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            cluster = MongoClient(
                "Your Connection String Here", tlsCAFile=certifi.where())
            db = cluster["socialMedia"]["messages"]
            all = db.find({})
            date = datetime.now().strftime("%x")

            if keywords[i] == "tweetBookRefresh":
                for messages in all:
                    try:
                        if date == messages["date"]:
                            await message.channel.send(f"Today - {messages['time']}")
                            await message.channel.send(f"Post ID: {messages['count']}")
                            await message.channel.send(f"From: {messages['id']}")
                            await message.channel.send(f"Message: {messages['message']}")
                            await message.channel.send(f"----------------------")
                        else:
                            await message.channel.send(f"{messages['date']} - {messages['time']}")
                            await message.channel.send(f"Post ID: {messages['count']}")
                            await message.channel.send(f"From: {messages['id']}")
                            await message.channel.send(f"Message: {messages['message']}")
                            await message.channel.send(f"----------------------")
                    except:
                        pass
            elif keywords[i] == "tweetBookAdd":
                count = db.count_documents({})

                initString = message.content
                word = "tweetBookAdd "
                newString = initString.replace(word, "")

                time = datetime.now().strftime("%X")
                person = "tweetBook Discord Bot"

                msg = {"count": count + 1, "id": person, "message": newString, "date": date, "time": time}
                db.insert_one(msg)

                await message.channel.send("Success")

            elif keywords[i] == "%help":
                await message.channel.send("I am the official tweetBook bot. Depending on the trigger word, "
                                           "I can either pull messages from my database or add messages to my database")
                await message.channel.send("More info at https://snolte26.github.io/tweetBook/")
            else:
                await message.channel.send("IDK how, but you triggered a command that doesn't exist, or hasn't been "
                                           "programmed")


client.run('Your token here')

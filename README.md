# tweetBook
A basic social media platform with some functionalities

This small social media platform was based on this video:
     https://www.youtube.com/watch?v=8TpRqjVlQSo

Creating this requires a MongoDB account. I sugesst watching the 
video above to do so and get a better understanding of whats happening.
Line 13, you will need to put your own connection string

On line 5 of the autoMod, you will need to input your own connection string.
The autoMod goes through the database and deletes posts that are 
older than 1 month, though this can be modified to fit your needs.

Both the AutoMod and TweetBokk are required for this to work properly.

To distribute to those without python, you must convert both the tweetBook app 
and the autoMod into .exe formats. This can be done by installing pyinstaller,
going into the command prompt navigating to the directory, and typing 
`pyinstaller --onefile pythonScriptName.py`

Users will need to set up a username and password to access the tweetBook when
first running the application. Login information is saved locally to the users
computer in the same directory as the application. Changing username and password 
involves opening the document with the username and password and manually 
changing it there.

Users are able to create a new post, refresh for new/incoming posts, view just their
own posts, see the posts of a certain user, delete their own posts, or quit the app.

````````````````````````````
Update 03/09/2021:
Added search users, view your posts, and delete your posts

Users can now search for other users to see their posts, view just 
their posts, and delete certain posts of theirs
````````````````````````````
````````````````````````````
Update 03/15/2021:
Added the AutoMod

After the user logs in, The program will run the AutoMod script that goes 
through the database and deletes posts older than 1 month. Previously the users
had to manually delete posts or wait for the database administrator to 
remove all the posts, and if the database filled up, you couldn't make any more
posts. Now users can moderate themselves and free up room in thedatabase as 
time moves forward.

````````````````````````````
````````````````````````````
Update 06/3/2021:
Added color, certification

Added some more color to the command line, making the ascii art blue instead of white on black 
background. added certification to "cluster = MongoClient()". After some failures to connect to 
a mongoDB database, extra certification was added to ensure connectivity
````````````````````````````

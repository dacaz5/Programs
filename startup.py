#Use the Task Scheduler (or a similar program) to have this file open on startup. Made by badooga.
from os import startfile
from os import listdir
from getpass import getuser
from time import ctime
from functions import input_str as pstr
from functions import input_question as pq
from functions import input_num as pn
from re import split as rsplit

hour = int(ctime().split()[3][:2])

def natural_key(string_): #used to properly sort file names
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in rsplit(r'(\d+)', string_)]

#Edit these variables if you want to customize them - for example, you may store your music in a different folder, or you may not want to be referred to by your account username
user = getuser()
filepath_playlists = "C:\\Users\\{}\\Music\\Playlists\\".format(user)
filepath_songs = "C:\\Users\\{}\\Music\\Songs\\".format(user)

if hour < 12:
    print("Good morning, {}.".format(user))
elif hour > 18:
    print("Good evening, {}.".format(user))
else:
    print("Good afternoon, {}.".format(user))

#keep in mind that for user input, I'm starting at 1 and not 0 for the sake of typing ease
def music(playlist_extension="", song_extension=""): #by default file extensions must be inputed manually by user; the other option is that you can put in a file extension as the parameter at the bottom where the function is called, including the '.'
    choice = pn("Would you like to play a playlist (1), a specific song (2), or remain silent (3)? ", int, 1, 3)
    loop = [False, False, False]
    loop[choice - 1] = True
    while loop[0]:
        choice = pstr("What music playlist would you like to play (enter 0 to cancel)? ", True, 1, True)
        if choice == "0":
            loop[0] = False
        else:
            try:
                startfile(filepath_playlists + choice + playlist_extension)
                loop[0] = False
            except:
                try: #if you typed in an int and it wasn't found as a music playlist, this program will automatically iterate through the folder and open that number
                    if int(choice) == float(choice) and int(choice) >= 1:
                        playlist_choice = int(choice) - 1
                    playlist_list = sorted(listdir(filepath_playlists), key=natural_key)
                    startfile(filepath_playlists + playlist_list[playlist_choice])
                    loop[0] = False
                except:
                    print("Error: File not found.")
    while loop[1]:
        choice = pstr("What music file would you like to play (enter 0 to cancel)? ", True, 1, True)
        if choice == "0":
            loop[1] = False
        else:
            try:
                startfile(filepath_songs + choice + song_extension)
                loop[1] = False
            except:
                try: #if you typed in an int and it wasn't found as a music file, this program will automatically iterate through the folder and open that number
                    if int(choice) == float(choice) and int(choice) >= 1:
                        song_choice = int(choice) - 1
                    song_list = sorted(listdir(filepath_songs), key=natural_key)
                    startfile(filepath_songs + song_list[song_choice])
                    loop[1] = False
                except:
                    print("Error: File not found.")



exit = False
while not exit:
    print("\nCommands: Quit (1), Music (2)")
    command = pn("Command: ", int, 1)
    if command == 1:
        exit = True
    elif command == 2:
        music()
    else:
        print("Invalid command. Please try again.")
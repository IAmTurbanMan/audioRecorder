import audio
import os

LOCAL_PATH = "/home/pi/Development/projects/audioRecorder"
DEST_PATH = "/audioFileUploader"
SCRIPT_PATH = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh"
selection = ""

while (selection.upper() != "X"):
    os.system("clear")
    print("""
#############################################
# Welcome to an Audio Recording Experience  #
#                                           #
# Please make a selection from below:       #
#                                           #
# 1. Record audio                           #
# 2. List files                             #
# 3. Upload audio                           #
# X. Exit                                   #
#                                           #
#############################################
    """)
    selection = input("Selection: ")

    if selection == "1":
        os.system("clear")
        os.system("cd {}".format(LOCAL_PATH))
        print("Recording... Press Enter to end recording.")
        audio.record()
        wavFileName = input("Enter a filename: ")
        if wavFileName[-4:] != '.wav':
	        wavFileName = wavFileName + '.wav'
	        wavFileName = wavFileName.replace(' ', '')

        audio.saveAudio(wavFileName)

    if selection == "2":
        os.system("clear")
        for root, dirs, files in os.walk(LOCAL_PATH):
            for file in files:
                if file.endswith(".wav"):
                    print(os.path.join(root, file))

    if selection == "3":
        os.system("clear")
        for root, dirs, files in os.walk(LOCAL_PATH):
            for file in files:
                if file.endswith(".wav"):
                    print(os.path.join(root, file))
                    fileToUpload = (os.path.join(root, file))
                    os.system("{} upload {} {}".format(SCRIPT_PATH, fileToUpload, DEST_PATH))

import sys
import os
import base64


def insert_data(string, data, every):  # Function to insert data
    return data.join(string[i:i+every] for i in range(0, len(string), every))


if len(sys.argv) < 2:  # Make sure that people actually give the dang script files.
    print('To make a Self Extracting Archive, drag the files you want to put together onto this file. Or, if your on the command line, just do DAT2BAT <file>')
    input('Press enter to exit')
else:

    usePass = 0  # Determine whether to use a password. Right here so the for loop can reach it without overriding it

    archivename = os.path.splitext(sys.argv[1])[0] + ".bat"

    for x in range(len(sys.argv) - 1):
        # Determine whether we use passwords
        if sys.argv[x + 1] == "-pass":
            usePass = 1
            archivename = os.path.splitext(sys.argv[3])[0] + ".bat"
            continue
        if usePass == 1 and x == 1:
            continue
        # Read
        filename = sys.argv[x + 1]  # Get file
        filestream = open(filename, "rb")  # Create a file stream
        filedata = filestream.read()  # Read raw bytes of file
        filestream.close()
        # Compress and encode data
        nfiledata = base64.b64encode(filedata)  # Encode data in Base64

        # Get ready to write
        if os.path.exists(filename):
            nfilestream = open(archivename, "a")
        else:
            nfilestream = open(archivename, "w")

        # Split Base64 data at every 8000th character so a cmd line doesnt get too long
        nfiledata = insert_data(str(nfiledata), " >> temp\r\necho ", 8000)
        # Format data into batch using magic
        if usePass == 1:
            nfilestream.write("@echo off\r\n:wrong\r\nset /p psw=Password? : \r\nif %psw% == " + sys.argv[2] + " goto :correct\r\ngoto :wrong\r\n:correct\r\necho " + str(nfiledata).replace("b'", "").replace("'", "") + " >> temp\r\ncertutil -decode temp " + os.path.split(filename)[1] + "\r\ndel temp -y\r\n:end\r\n")
        else:
            nfilestream.write("echo " + str(nfiledata).replace("b'", "").replace("'", "") + " >> temp\r\ncertutil -decode temp " + os.path.split(filename)[1] + "\r\ndel temp -y")

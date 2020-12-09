import sys
import os
import base64


def insert_data(string, data, every):  # Function to insert data
    return data.join(string[i:i+every] for i in range(0, len(string), every))


if len(sys.argv) < 2:  # Make sure that people actually give the dang script files.
    print('To make a Self Extracting Archive, drag the files you want to put together onto this file. Or, if your on the command line, just do DAT2BAT <file>')
    input('Press enter to exit')
else:

    archivename = os.path.splitext(sys.argv[1])[0] + ".zsh"

    for x in range(len(sys.argv) - 1):
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
        nfiledata = insert_data(str(nfiledata), " > temp\necho ", 8000)
        # Format data into batch using magic
        nfilestream.write("echo " + str(nfiledata).replace("b'", "").replace("'", "") + " > temp\nbase64 -d temp > " + os.path.split(filename)[1] + "\nrm temp")
print('Please keep in mind that to use the archive you must use homebrew to install GNU coreutils!!!')
input('Press enter to exit')

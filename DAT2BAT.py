import sys
import os
import base64


def insert_data(string, data, every):
    return data.join(string[i:i+every] for i in range(0, len(string), every))


if len(sys.argv) < 2:  # Make sure that people actually give the dang script files.
    print('To make a Self Extracting Archive, drag the files you want to put together onto this file. Or, if your on the command line, just do DAT2BAT <file>')
    input('Press enter to exit')
else:
    for x in range(len(sys.argv) - 1):
        filename = sys.argv[x + 1]  # Get file
        filedata = open(filename, "rb").read()  # Read raw bytes of file

        nfiledata = base64.b64encode(filedata)
        if os.path.exists(filename):
            nfilestream = open("Archive.bat", "a")
        else:
            nfilestream = open("Archive.bat", "w")

        nfilestream.write(insert_data("echo " + str(nfiledata).replace("b'", "").replace("'", "") + " >> temp\r\ncertutil -decode temp " + os.path.split(filename)[1] + "\r\ndel temp -yr\r\n", " >> temp\r\necho ", 8000))

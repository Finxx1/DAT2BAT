# NOTE: I wrote this in python after finding out that the MEMZ trojan came in a batch file. Looking through the source code to MEMZ using the wayback
# machine,  I found he used a python script to make the batch file. However, he used python 2 to make it. While trying to clean it up, I got so annoyed
# that I though I would be better off remaking it from scratch. For some reason, I stuck with python instead of moving to C (my main language). So this
# is what I ended up with. I tested with ASCII files as I was using a windows 7 VM that did not have a hex editor and therefor did not take raw bytes
# in to consideration. I made this in 2 days and probably spent 5 hours total actually working on it. I am currently working on making a better version
# also in python (because as Michael Reeves once said, "Python can do anything, just badly." and I really wanna overengineer this dumb idea.)

import sys
import os

if len(sys.argv) < 2: # Make sure that people actually give the dang script files.
    print('To make a Self Extracting Archive, drag the files you want to put together onto this file one at a time.')
    input('Press enter to exit')
else:
    for x in range(len(sys.argv) - 1):  # We cannot set the starting value of x, so we make the number of loops less
        filename = sys.argv[x + 1]  # We have to add 1 to make up for the fact that we start on loop 0
        filedata = open(filename, "rb").read()  # Read the file's data. Even though we read the binary, it has to be text
        nfilename = "Archive.bat"  # Name the archive. Might make this a command line parameter.
        if os.path.exists(nfilename):  # Check if the file exists so we know to append instead of write over
            nfilestream = open(nfilename, "a")
        else:
            nfilestream = open(nfilename, "w")
        # WARNING: I WROTE THIS LINE YESTERDAY I HAVE NO IDEA HOW THE HECK IT WORKS
        nfilestream.write("echo " + str(filedata).replace('|', '^|').replace('<', '^<').replace('>', '^>').replace('\\t', '\t').replace('\\r\\n', ' >> ' + os.path.split(filename)[1] + '\r\necho ').removeprefix("b'").removesuffix("'") + " >> " + os.path.split(filename)[1] + "")
        # Remove the 'ECHO is on.' text that is written when you want to make a blank line. PowerShell is the only way
        # to find and replace text using Batch according to StackOverflow
        nfilestream.write('''\r\npowershell -Command "(gc ''' + os.path.split(filename)[1] + ''') -replace 'ECHO is on.', '' | Out-File -encoding ASCII ''' + os.path.split(filename)[1] + '''"\r\n''')

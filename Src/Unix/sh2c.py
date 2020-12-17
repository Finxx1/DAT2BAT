# The compiler for bARC. Takes in a batch file and formats it into a .c file. Hopefully could be compiled by gcc and tcc.

import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]  # Get file
    filestream = open(filename, "rb")  # Create a file stream
    filedata = filestream.read()  # Read raw bytes of file
    filestream.close()
    # Get ready to write
    if os.path.exists(filename):
        nfilestream = open(filename + ".c", "a")
    else:
        nfilestream = open(filename + ".c", "w")
    nfilestream.write('#include <stdio.h>\nint main() {\nsystem("' + str(filedata).removeprefix("b'").removesuffix("'").replace("\\n", '");\nsystem("') + '");\nreturn 0;\n}')
else:
    print("To compile a batch file, please drag the file onto this file.")
    input("Press enter to exit")

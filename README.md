# bARC
![](Img/logo.png)
---
A data archiving utility

## How do I use it?
You can get binaries [here](https://github.com/Finxx1/DAT2BAT/releases) and just drag files on to ```bARC.exe```. However, if the exe does not work, use the below steps.
### Prerequisites
Install python [here](https://www.python.org/downloads/), making sure to select Add Python (Version) to PATH.
### Method 1.
1. Clone this repo
2. Right-click the bARC.py file and click properties
3. Press the button that says ```CHANGE```
4. Select ```Python```
5. Press ```OK```
6. Select the files you want to archive.
7. Drag them on to bARC.py
### Method 2.
1. Open Command Prompt
2. Navigate to the folder containing bARC.py
3. Type ```py bARC.py <file(s)>```
---
If you followed the steps correctly, you will end up with a batch script that can work even without bARC, making it perfect for sharing multiple files with other people in an easy and efficient way.

## Passwords

To make an archive require a password, you have to use the command line. Typing ```py bARC.py -pass <password> <file(s)>``` will give you an archive that requires a password to open.

## How does it work?
The Python script takes in any number of files and outputs a batch script. The batch script works by echo-ing the Base64 data of the files archived by bARC into a file called ```temp```. Then, we call ```certutil -decode```. This program comes bundled with windows 7, 8, 8.1, and 10. It decodes the data and outputs it as a file with the same name as the archived file. For more info, check out [this](Doc/DEV.md)

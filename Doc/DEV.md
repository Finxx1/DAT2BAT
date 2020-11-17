# So, you wanna know how it works? Cool! 

The Python script has 3 main parts:

1. The code that reads the data from the files you gave it.
2. The code that converts it to Base64.
3. The code that formats the data into valid batch data

## Part 1 in greater detail

We start by getting command line input. Because sys.argv[] starts with the name of the script, we have to use +1 to get the data. This means we have to stop the loop 1 before it was supposed to end. Then we store that value in a variable called ```filename```. We then make a new variable called ```filestream``` and set it's value to the returned data of
```python
open(filename, "rb")
```

We use "rb" so that we read the data in bytes, not ASCII, as that can cause data loss. After we open for reading, we make a new variable called ```filedata``` equal to

```python
filestream.read()
```

We then close ```filestream``` with

```python
filestream.close
```

## Part 2 in greater detail

This is just one line, so I will make this quick:

```python
nfiledata = base64.b64encode(filedata)
```

We create a variable called ```nfiledata``` and set it's value to the returned bytes of ```base64.b64encode(filedata)```. This gives us Base64 encoded data.

## Part 3 in greater detail

Considering that I, the creator, doesn't even know how the 4 lines of code work, I think it would be better to look at the result. I just gave the script ```doc.txt```.

```batch
echo REFUMkJBVCBpcyBhIHByb2dyYW0gdGhhdCBtYWtlcyBTZWxmLUV4dHJhY3RpbmcNCkFyY2hpdmVzLiBTaW1wbHkgZHJhZyBmaWxlcyBvbiB0byAnREFUMkJBVC5weScuDQpJZiB5b3UgYXJlIHVzaW5nIHRoZSBjb21tYW5kIGxpbmUsIHNpbXBseSB0eXBlDQonREFUMkJBVC5weSAnIGZvbGxvd2VkIGJ5IGFueSBhbW91bnQgb2YgZmlsZXMuDQpJbiB0aGUgY29tbWFuZCBsaW5lLCB5b3UgY2FuIHNldCBhIHBhc3N3b3JkIGZvcg0KdGhlIGFyY2hpdmUgYnkgdHlwaW5nICctcGFzcyA8UEFTU1dPUkQ+JyB0aGlzDQp3b3VsZCBsb29rIGxpa2UNCidweXRob24gREFUMkJBVC5weSAtcGFzcyAxMjM0NTYgZGF0YS5kYXQn >> temp

certutil -decode temp doc.txt

del temp -y
```

The first line is the Base64 data. We are using echo to write it to a file called ```temp```. Next, we are calling ```certutil -decode```. This takes a file with Base64 and outputs it to another file. In this case, it is outputting the data to ```doc.txt```. Finally, we delete the temp file with ```del temp -y```. We use -y so that it does not ask us if we are sure.
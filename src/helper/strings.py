def textToAscii(str):
    return [ord(c) for c in str]

def asciiToText(ascii):
    str = ""
    for i in ascii:
        str = str + chr(i)
    return str
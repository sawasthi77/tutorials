def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me 415-555-1011 tomorrow or 415-555-9999 to connect with me on my office line.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any numbers.')


#print(isPhoneNumber('415-555-1234'))

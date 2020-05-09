import re

message = 'Call me 415-555-1011 tomorrow or 415-555-9999 to connect with me on my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(message)
mo1 = phoneNumRegex.findall(message)

print(mo.group())
print(mo1.group())

while True:
    print('Please enter your name')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password?(Is it a fish?)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')

        
seq = ['soup', 'dog', 'salad', 'cat', 'great']

#t = lambda l: list(map(l, seq))

print(list(filter(lambda l: l[0] == 's', seq)))

def my_fun(speed, isBirthday):
    if isBirthday == 'False':
        if speed <=60:
            print('No ticket')
        elif speed > 60 and speed <= 80:
            print('Small Ticket')
        elif speed > 80:
            print('Big Ticket')
    else:
        if speed <=65:
            print('No ticket')
        elif speed > 65 and speed <= 85:
            print('Small Ticket')
        elif speed > 85:
            print('Big Ticket')
    
my_fun(30, True)

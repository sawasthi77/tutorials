def my_func(num):
    return num*2

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

seq = [1, 2, 3, 4, 5]
print(list(map(my_func, seq)))

print(list(map(lambda num: num *2, seq)))

print(list(filter(lambda num: num%2 == 0, seq)))

print(list(filter(even, seq)))
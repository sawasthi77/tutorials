def my_func(name = 'Deafult name'):
    print('Hello ' + name)

my_func()

def square(num):
    
    """This is a huge comment or string inside a function that can be called 
        through a signature function. 
     """
    return num**2
output = square(2)
print(output)
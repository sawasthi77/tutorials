import random
print('I am thinking a number between 1 and 20.')
secretNumber = random.randint(1, 20)
numberofguesses = 0
for numberofguesses in range(1, 20):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        print('Good Job! You guessed my number in ' + str(numberofguesses) + ' guesses.')
        break    

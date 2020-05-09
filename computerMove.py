import random

randomMove = str(random.randint(1, 3))
if randomMove == '1':
    computerMove = 'r'
    print('ROCK')
    if playerMove == computerMove:
        print('It is a tie')
        ties += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You loose!! Try again')
        losses += 1
elif randomMove == '2':
    computerMove = 'p'
    print('PAPER')
    if playerMove == computerMove:
        print('It is a tie')
        ties += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win !')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You loose!! Try again')
        losses += 1
elif randomMove == '3':
    computerMove = 's'
    print('SCISSORS')
    if playerMove == computerMove:
        print('It is a tie')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win !')
        wins += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You win !')
        wins += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You loose!! Try again')
        losses += 1







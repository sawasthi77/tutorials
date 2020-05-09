import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0; losses = 0; ties = 0
#taking into account player move
while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove = input()
    if playerMove == 'q':
        sys.exit
    elif playerMove == 'r':
        print('ROCK versus')
        break
    elif playerMove == 'p':
        print('PAPER versus')
        break
    elif playerMove == 's':
        print('SCISSORS versus')
        break
#taking into account computer move

randomMove = str(random.randint(1, 3))
if randomMove == '1':
    computerMove = 'r'
    print('ROCK')
elif randomMove == '2':
    computerMove = 'p'
    print('PAPER')
elif randomMove == '3':
    computerMove = 's'
    print('SCISSORS')
print(computerMove)
#Now deciding who wins and looses
if playerMove == computerMove:
    print('It is a tie')
    ties += 1
elif playerMove == 'r' and computerMove == 's':
    print('You Win !')
    wins += 1
elif playerMove == 'p' and computerMove == 's':
    print('You win !')
    wins += 1
elif playerMove == 's' and computerMove == 'p':
    print('You win !')
    wins += 1
elif playerMove == 's' and computerMove == 'r':
    print('You loose!! Try again')
    losses += 1
elif playerMove == 'r' and computerMove == 'p':
    print('You loose!! Try again')
    losses += 1
elif playerMove == 'p' and computerMove == 's':
    print('You loose!! Try again')
    losses += 1

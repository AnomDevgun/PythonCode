from random import shuffle

def guess(guessList,playerPos):
    shuffle(guessList)
    if(guessList[playerPos]=='O'):
        return (guessList,True)
    else:
        return (guessList,False)

playerPosition = -1
while playerPosition not in [1,2,3]:
    playerPosition = int(input('Please enter a position, 1, 2 or 3 : '))
    if(playerPosition==1 or playerPosition==2 or playerPosition==3):
        print('You have entered a valid position\n')
        retList,boolPlayer = guess([' ','O',' '],playerPosition-1)
        print(f'The randomly shuffled list was {retList} and you guessed position: {playerPosition}')
        if boolPlayer:
            print('Congratulations! You guessed the position correctly\n')
        else:
            print('Sorry, your guess was incorrect, please try again!\n')
    else:
        print('Please enter a valid position\n')
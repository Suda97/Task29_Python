import os


## Checking for 3 same numbers in the row
def check(gamelist):
    if gamelist[0][0] == gamelist[0][1] == gamelist[0][2] == 1:
        return 1
    elif gamelist[0][0] == gamelist[0][1] == gamelist[0][2] == 2:
        return 2

    if gamelist[1][0] == gamelist[1][1] == gamelist[1][2] == 1:
        return 1
    elif gamelist[1][0] == gamelist[1][1] == gamelist[1][2] == 2:
        return 2

    if gamelist[2][0] == gamelist[2][1] == gamelist[2][2] == 1:
        return 1
    elif gamelist[2][0] == gamelist[2][1] == gamelist[2][2] == 2:
        return 2

    if gamelist[0][0] == gamelist[1][0] == gamelist[2][0] == 1:
        return 1
    elif gamelist[0][0] == gamelist[1][0] == gamelist[2][0] == 2:
        return 2

    if gamelist[0][1] == gamelist[1][1] == gamelist[2][1] == 1:
        return 1
    elif gamelist[0][1] == gamelist[1][1] == gamelist[2][1] == 2:
        return 2

    if gamelist[0][2] == gamelist[1][2] == gamelist[2][2] == 1:
        return 1
    elif gamelist[0][2] == gamelist[1][2] == gamelist[2][2] == 2:
        return 2

    if gamelist[0][0] == gamelist[1][1] == gamelist[2][2] == 1:
        return 1
    elif gamelist[0][0] == gamelist[1][1] == gamelist[2][2] == 2:
        return 2

    if gamelist[0][2] == gamelist[1][1] == gamelist[2][0] == 1:
        return 1
    elif gamelist[0][2] == gamelist[1][1] == gamelist[2][0] == 2:
        return 2


## Printing whole game board
def printGame(gamelist):
    for i in range(0, 3):
        print(*gamelist[i])


## Player one round
def playerOneRound(gamelist):
    while True:
        x = int(input("Player ONE turn!\nX cord: ")) - 1
        y = int(input("Y cord: ")) - 1
        if gamelist[x][y] == 0:  ## checking if the field is taken if not then change number
            gamelist[x][y] = 1
            break
        else:
            os.system('clear')
            print("Place taken! Choose another")
            printGame(gamelist)
    os.system('clear')
    return gamelist


## Player two round
def playerTwoRound(gamelist):
    while True:
        x = int(input("Player TWO turn!\nX cord: ")) - 1
        y = int(input("Y cord: ")) - 1
        if gamelist[x][y] == 0:
            gamelist[x][y] = 2
            break
        else:
            os.system('clear')
            print("Place taken! Choose another")
            printGame(gamelist)
    os.system('clear')
    return gamelist


## Whole game script
def game(gamelist, score):
    count = 0
    while True:
        printGame(gamelist)
        gamelist = playerOneRound(gamelist)
        count += 1
        if check(gamelist) == 1:
            printGame(gamelist)
            print("PLAYER ONE WINS!")
            score[0] += 1
            break
        if count == 5:
            print("TIE!")
        printGame(gamelist)
        gamelist = playerTwoRound(gamelist)
        if check(gamelist) == 2:
            printGame(gamelist)
            print("PLAYER TWO WINS!")
            score[1] += 1
            break
    return score


if __name__ == '__main__':
    score = [0, 0]
    while True:
        gamelist = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        score = game(gamelist, score)
        print("Score:   P1: " + str(score[0]) + "   P2: " + str(score[1]))
        ans = int(input("Do You want to keep playing?\nType 1 if YES\nType 2 if NO\n"))
        if ans == 2:
            break
        os.system('clear')
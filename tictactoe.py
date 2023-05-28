
## Create a Board
def board(xState, zeroState):
    zero =   'X' if xState[0] == 1 else 'O' if zeroState[0] == 1 else 0
    one =    'X' if xState[1] == 1 else 'O' if zeroState[1] == 1 else 1
    two =    'X' if xState[2] == 1 else 'O' if zeroState[2] == 1 else 2
    three =  'X' if xState[3] == 1 else 'O' if zeroState[3] == 1 else 3
    four =   'X' if xState[4] == 1 else 'O' if zeroState[4] == 1 else 4
    five =   'X' if xState[5] == 1 else 'O' if zeroState[5] == 1 else 5
    six =    'X' if xState[6] == 1 else 'O' if zeroState[6] == 1 else 6
    seven =  'X' if xState[7] == 1 else 'O' if zeroState[7] == 1 else 7
    eight =  'X' if xState[8] == 1 else 'O' if zeroState[8] == 1 else 8
    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")

## Check for Win 
def checkwin(xState,zeroState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:
        if xState[win[0]] == 1 and xState[win[1]] == 1 and xState[win[2]] == 1:
            print('X Wins')
            return 1
        elif zeroState[win[0]] == 1 and zeroState[win[1]] == 1 and zeroState[win[2]] == 1:
            print('0 Wins')
            return 0

## Main Function

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zeroState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X, 0 for 0
    moves = 0
    print('Welcome to Tic Tac Toe!')
    while True:
        board(xState, zeroState)
        if turn == 1:
            print('X Chance')
            value = int(input('Enter the position: '))
            xState[value] = 1
        else:
            print('0 Chance')
            value = int(input('Enter the position: '))
            zeroState[value] = 1
        check = checkwin(xState, zeroState)
        moves += 1
        if check == 1:
            break
        elif check == 0:
            break
        elif moves == 9:
            print('Draw')
            break
        turn = 1 - turn
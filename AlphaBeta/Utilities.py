XPLAYER = +1
OPLAYER = -1

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def printOut(brd):
    chars = {XPLAYER: 'X', OPLAYER: 'O', 0: ' '}
    print('---------------')
    for x in brd:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n' + '---------------')
    print('+++++++++++++++\n')

def printResult(brd):
    if winner(brd, XPLAYER):
        print('X wins!\n')
    elif winner(brd, OPLAYER):
        print('O wins!\n')
    else:
        print('Draw\n')

def winner(brd, player_value):
    winningStates = [[brd[0][0], brd[0][1], brd[0][2]], #1st row
                     [brd[1][0], brd[1][1], brd[1][2]], #2nd row
                     [brd[2][0], brd[2][1], brd[2][2]], #3rd row
                     [brd[0][0], brd[1][0], brd[2][0]], #1st column
                     [brd[0][1], brd[1][1], brd[2][1]], #2nd column
                     [brd[0][2], brd[1][2], brd[2][2]], #3rd column
                     [brd[0][0], brd[1][1], brd[2][2]], #diagonal - top left to bottom right
                     [brd[0][2], brd[1][1], brd[2][0]]] #diagonal - top right to bottom left
    if [player_value, player_value, player_value] in winningStates: #if 3 in a row
        return True
    return False


def won(brd):
    return (winner(brd, XPLAYER) or winner(brd, OPLAYER))


def emptyCells(brd):
    emptyC = []
    for x in range(3):
        for y in range(3):
            if brd[x][y] == 0:
                emptyC.append([x, y])
    return emptyC


def boardFull(brd):
    if len(emptyCells(brd)) == 0:
        return True
    return False


def setMove(brd, x, y, player):
    brd[x][y] = player


def humanMove(brd):
    bad_input = True
    positions = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                4: [1, 0], 5: [1, 1], 6: [1, 2],
                7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while bad_input:
        try:
            in_pos = int(input('Pick a position(1-9): '))
            if in_pos > 9 or in_pos < 1:
                print('Invalid location! ')
            elif positions[in_pos] not in emptyCells(brd):
                print('Location filled ')
            else:
                setMove(brd, positions[in_pos][0], positions[in_pos][1], XPLAYER)
                printOut(brd)
                bad_input = False
        except(KeyError, ValueError):
            print('Please pick a number! ')


def getScore(brd):
    if winner(brd, XPLAYER):
        return -10
    elif winner(brd, OPLAYER):
        return 10
    else:
        return 0
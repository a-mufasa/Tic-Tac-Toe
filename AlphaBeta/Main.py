from random import choice
from math import inf
import time
from alphabeta import *

def AIMove(brd):
    if len(emptyCells(brd)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        setMove(brd, x, y, OPLAYER)
        printOut(brd)
    else:
        start = time.time()
        result = alphaBeta(brd, len(emptyCells(brd)), -inf, inf, OPLAYER)
        end = time.time()
        setMove(brd, result[0], result[1], OPLAYER)
        print("AlphaBeta Runtime:", end-start, "s")
        printOut(brd)


def main():
    print('Player vs AI using ALPHABETA Algorithm\n')
    while True:
        try:
            turn = int(input('Are you playing 1st or 2nd? (1/2) '))
            if not (turn == 1 or turn == 2):
                print('Pick 1 (first) or 2 (second)')
            else:
                break
        except(ValueError, KeyError):
            print('Please properly enter a number')
    if turn == 1:
        currentPlayer = XPLAYER
    else:
        currentPlayer = OPLAYER

    while not (boardFull(board) or won(board)):
        if currentPlayer == XPLAYER:
            humanMove(board)

        else:
            AIMove(board)
        currentPlayer *= -1 #alternates turn (+1 becomes -1 & vice versa)

    printResult(board)


if __name__ == '__main__':
    main()

from Utilities import *
from math import inf


def minMax(brd, depth, player):
    row = -1
    col = -1

    if won(brd) or len(emptyCells(brd))==0:
        return [row, col, getScore(brd), depth]
    
    if player == OPLAYER:
        move = (row, col, -inf, depth)
    else:
        move = (row, col, inf, depth)

    for cell in emptyCells(brd):
        setMove(brd, cell[0], cell[1], player)
        score = minMax(brd, depth+1, -player)
        setMove(brd, cell[0], cell[1], 0)
        score = (cell[0], cell[1], score[2], score[3])
        
        if player == OPLAYER and (score[2] > move[2] or (score[2] == move[2] and score[3] < move[3])):
            move = score
        elif player == XPLAYER and (score[2] < move[2] or (score[2] == move[2] and score[3] < move[3])):
            move = score
            
    return move
from Utilities import *
from math import inf

def alphaBeta(brd, depth, a, b, player):
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
        score = alphaBeta(brd, depth+1, a, b, -player)
        setMove(brd, cell[0], cell[1], 0)
        score = (cell[0], cell[1], score[2], score[3])
        
        if player == OPLAYER:
            if score[2] > move[2] or (score[2] == move[2] and score[3] < move[3]):
                move = score
            if (move[2] >= b) and score[3] >= depth:
                break
            a = max(a, move[2])
        else:
            if score[2] < move[2] or (score[2] == move[2] and score[3] < move[3]):
                move = score
            if (a >= move[2]) and score[3] >= depth:
                break
            b = min(b,move[2])
            
    return move


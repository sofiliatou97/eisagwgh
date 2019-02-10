from random import *

# 3x3 gameboard
gameboard = [(['.']*3) for i in range(3)]
row_col = [0]
turn = 1

def input_valid(values):
    global player
    if len(values) != 2:
        print "Input format: row,col (ex.1,2)"
        return 0
    try:
        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
            # check for filled pos
            if gameboard[int(values[0])-1][int(values[1])-1] != '.':
                if player == 1:
                    print "Position taken."
                return 0
            return 1
        else:
            print "Input numbers: 1,2,3"
            return 0
    except ValueError:
        print "Input numbers: 1,2,3"
        return 0


def draw_board(values, player):
    gameboard[int(values[0])-1][int(values[1])-1]=player
    for row in gameboard:
	print row

def win_by_Column():
    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i]:
            if gameboard[0][i] == '.':
                continue
            elif gameboard[0][i] == 'X':
                print "Player wins!"
                quit()
            else:
                print "Computer wins!"
                quit()
            return 1

def win_by_diagonal():
    if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]) or (gameboard[0][2] == gameboard[1][1] == gameboard[2][0]): 
        if gameboard[1][1] == 'X':
            print "Player wins!"
            quit()
        elif gameboard[1][1] == 'O':
            print "Computer wins!"
            quit()
        else:
            return 0
        return 1

def win_by_row():
    for i in range(3):
        if len(set(gameboard[i])) == 1:
            if gameboard[i][1] == '.':
                continue
            elif gameboard[i][1] == 'X':
                print "Player wins!"
                quit()
            else:
                print "Computer wins!"
                quit()
            return 1

def game_over():
    searcht = '.'
    
    # check win by column
    win_by_Column()

    # check win by diagonal
    win_by_diagonal()

    # check win by row
    win_by_row()
    
    # check board is full
    for sublist in gameboard:
        if searcht in sublist:
            return 0

    print "Game over! No more moves avaliable"
    return 1


# Main
roundNumber = 0
while not game_over():
    piece = '.'
    while not input_valid(row_col):
        player = turn % 2
        if player == 0:
            player = 2
            list = ['1,1','1,2','1,3','2,1','2,2','2,3','3,1','3,2','3,3']
            p1 = list[randint(0, 8)]
            piece = 'O'
        else:
            piece = 'X'
            p1 = raw_input('Player' + ' input: ')
            roundNumber = roundNumber + 1
        row_col = p1.split(",")


    draw_board(row_col, piece)

    row_col = [0]
    turn += 1

0
default = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]]


# convert int to (i, j)
def convert_int_to_ij(number):
    i = number // 3
    j = number % 3
    return (i, j)

def display_board(board):
    top = '+-------+-------+-------+'
    mid = '|       |       |       |'
    for row in board:
        var = f'|   {row[0]}   |   {row[1]}   |   {row[2]}   |'
    
        print(top, mid, var, mid, sep= "\n")
    print(top)


def make_list_of_free_fields(board):
    free_squares = []
    length = len(board)
    for i in board:
        for j in i:
            if isinstance(j, int):
                free_squares.append(j)
    return free_squares


def enter_move(board):
    free_squares = make_list_of_free_fields(board)
    print(free_squares)
    usr_inp = int(input('enter a valid integer: '))
    if usr_inp in free_squares:
        i, j = convert_int_to_ij(usr_inp)
        board[i][j] = 'O' 
    else:
        print("input invalid")


def victory_for(board, sign):
    # horizontals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True

    # verticals
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
        
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

import random

def draw_move(board):
    
    # get list of free fields
    free_squares = make_list_of_free_fields(board)
    # choose from one of the free field
    move = random.choice(free_squares)
    if len(free_squares) == 9:
        move = 4
    if move in free_squares:
        
        i, j = convert_int_to_ij(move)
        board[i][j] = 'X'

    



board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]


while True:
    available_move = len(make_list_of_free_fields(board)) > 0
    if available_move:
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print('X wins!')
            break
    else:
        print('Tie!')
        break
    if available_move:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print('O wins!')
            break
    else:
        print('Tie!')
        break
    


# In[ ]:





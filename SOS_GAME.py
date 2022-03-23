#    --------                           --------
#   |                                  |
#   |                -----------       |
#   |               |           |      |
#    --------       |           |       --------
#            |      |           |               |
#            |       -----------                |
#            |                                  |
#    --------                           --------
########################################################################################################################

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
score1 = 0
score2 = 0
n_action = 0
l = []
used_indexes = []
valid_symbols = ['s', 'o']


def display_board():
    print(" -----------------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " | ", board[3], " |")
    print(" -----------------------")
    print("| ", board[4], " | ", board[5], " | ", board[6], " | ", board[7], " |")
    print(" -----------------------")
    print("| ", board[8], " | ", board[9], "| ", board[10], "| ", board[11], "|")
    print(" -----------------------")
    print("| ", board[12], "| ", board[13], "| ", board[14], "| ", board[15], "|")
    print(" ------------------------")
    print('\n')


def action():
    diag1 = (board[0] == board[10]) and (board[5] == 'o')
    diag2 = (board[2] == board[8]) and (board[5] == 'o')
    diag3 = (board[1] == board[11]) and (board[6] == 'o')
    diag4 = (board[3] == board[9]) and (board[6] == 'o')
    diag5 = (board[4] == board[14]) and (board[9] == 'o')
    diag6 = (board[6] == board[12]) and (board[9] == 'o')
    diag7 = (board[5] == board[15]) and (board[10] == 'o')
    diag8 = (board[7] == board[13]) and (board[10] == 'o')

    row1 = (board[0] == board[2]) and (board[1] == 'o')
    row2 = (board[1] == board[3]) and (board[2] == 'o')
    row3 = (board[4] == board[6]) and (board[5] == 'o')
    row4 = (board[5] == board[7]) and (board[6] == 'o')
    row5 = (board[8] == board[10]) and (board[9] == 'o')
    row6 = (board[9] == board[11]) and (board[10] == 'o')
    row7 = (board[12] == board[14]) and (board[13] == 'o')
    row8 = (board[13] == board[15]) and (board[14] == 'o')

    col1 = (board[0] == board[8]) and (board[4] == 'o')
    col2 = (board[4] == board[12]) and (board[8] == 'o')
    col3 = (board[1] == board[9]) and (board[5] == 'o')
    col4 = (board[5] == board[13]) and (board[9] == 'o')
    col5 = (board[2] == board[10]) and (board[6] == 'o')
    col6 = (board[6] == board[14]) and (board[10] == 'o')
    col7 = (board[3] == board[11]) and (board[7] == 'o')
    col8 = (board[7] == board[15]) and (board[11] == 'o')
    return diag1 or diag2 or diag3 or diag4 or diag5 or diag6 or diag7 or diag8 or row1 or row2 or row3 or row4 or row5 or row6 or row7 or row8 or col1 or col2 or col3 or col4 or col5 or col6 or col7 or col8


def player_one():
    global score1, board, l

    display_board()
    print('PLAYER ONE')
    number = int(input('choose number from the board: '))

    while number in used_indexes:
        print(f'sorry {number} is used')
        number = int(input('choose number from the board and not used before: '))

    while number > 16 or number < 0:
        print(f'sorry {number} is out of the range')
        number = int(input('choose number from the board: '))

    l.append(number)
    used_indexes.append(number)

    symbol = input('which symbol do you want s or o: ')

    while symbol not in valid_symbols:
        print(f'sorry >> {symbol} << is not valid')
        symbol = input('which of the symbol you want s or o: ')

    board[number - 1] = symbol
    if action():
        score1 = score1 + 1
        print(f'the score of player one is: {score1}')
        for num in l:
            board[num - 1] = '*'
        l.clear()


def player_two():
    global score2, board, l

    display_board()
    print('PLAYER TWO')
    number = int(input('choose number from the board: '))

    while number in used_indexes:
        print(f'sorry {number} is used')
        number = int(input('choose number from the board and not used before: '))

    while number > 16 or number < 0:
        print(f'sorry {number} is out of the range')
        number = int(input('choose number from the board: '))

    l.append(number)
    used_indexes.append(number)

    symbol = input('which symbol do you want s or o: ')

    while symbol not in valid_symbols:
        print(f'sorry >> {symbol} << is not valid')
        symbol = input('which of the symbol you want s or o: ')

    board[number - 1] = symbol
    if action():
        score2 = score2 + 1
        print(f'the score of player two is: {score2}')
        for num in l:
            board[num - 1] = '*'
        l.clear()


def start_play():
    print('HELLO PLAYERS IN SOS GAME..')
    for i in range(0, 8):
        player_one()
        player_two()

    print('==========================================')

    print(f'the score of player one is: {score1}')
    print(f'the score of player two is: {score2}')

    if score1 > score2:
        print('########### the winner is PLAYER ONE ###########')
    elif score2 > score1:
        print('########### the winner is PLAYER TWO ###########')
    elif score1 == score2:
        print('they are equal')
        exit()


######################################
start_play()

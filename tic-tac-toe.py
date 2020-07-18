def start_game():
    start = input('\n\t\t*** Welcome to TIC TAC TOE ***\n\nWould you like to play(Please type Yes or No): ')
    if start == 'Yes' or start == 'yes' or start == 'YES':
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        choose_mark(board,num_board)
    else:
        exit()

def choose_mark(board,num_board):
    player_1_mark = input("It's great\nChoose X or O for player 1: ")
    if player_1_mark == 'X' or player_1_mark == 'x':
        marks = ['X','O']
    else:
        marks = ['O','X']
    print('Player 1 mark: {}\nPlayer 2 mark: {}'.format(marks[0],marks[1]))
    ref_disblay_baord(board)
    player1_input(marks,board,num_board)

def ref_disblay_baord(board):
    print('\nSample board:\n')
    print('| {} | {} | {} |'.format(board[0],board[1],board[2]))
    print('----+---+----')
    print('| {} | {} | {} |'.format(board[3],board[4],board[5]))
    print('----+---+----')
    print('| {} | {} | {} |'.format(board[6],board[7],board[8]))

def player1_input(marks,board,num_board):
    position = int(input('\nPlayer 1(mark {}), Please select position: '.format(marks[0])))
    if position in board:
        board[position-1] = ''
        num_board[position - 1] = marks[0]
    else:
        player1_input(marks,board,num_board)
    display_board(num_board)
    check_win(board,num_board,marks,1)

def player2_input(marks,board,num_board):
    position = int(input('Player 2(mark {}), Please select position: '.format(marks[1])))
    if position in board:
        board[position-1] = ''
        num_board[position - 1] = marks[1]
    else:
        player2_input(marks,board,num_board)
    display_board(num_board)
    check_win(board,num_board,marks,2)

def isDraw(board):
    list = []
    for x in range(1,10):
        if x in board:
            list.append(x)
        else:
            pass
    if len(list) == 0:
        return True

def check_win(board,num_board,marks,mark):
    if mark == 1:
        result = check_condition(num_board,marks[0])
        if result:
            print('\n\t\tCongratulation!!! Player 1 WON the match\n')
            start_game()
        elif isDraw(board) == True:
            print('\nMatch DRAW')
            start_game()
        else:
            player2_input(marks,board,num_board)
    else:
        result = check_condition(num_board,marks[1])
        if result:
            print('\nCongratulation!!! Player 2 WON the match\n')
            start_game()
        elif isDraw(board) == True:
            print('\nMatch DRAW')
            start_game()
        else:
            player1_input(marks,board,num_board)


def check_condition(board, mark):
    if (board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5] == mark) or (board[6] == board[7] == board[8] == mark) or (board[0] == board[3] == board[6] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark):
        return True
    else:
        return False

def display_board(board):
    print('\n| {} | {} | {} |'.format(board[0], board[1], board[2]))
    print('----+---+----')
    print('| {} | {} | {} |'.format(board[3], board[4], board[5]))
    print('----+---+----')
    print('| {} | {} | {} |\n'.format(board[6], board[7], board[8]))

start_game()

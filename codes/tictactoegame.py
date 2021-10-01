import random
from IPython.display import clear_output

#function for displaying the tic-tac-toe board.
def display_board(board):
    clear_output()  
    
    print('    |   | ')
    print("  {0} | {1} | {2}".format(board[7],board[8],board[9]))
    print('    |   | ')
    print('-----------')
    print('    |   | ')
    print("  {0} | {1} | {2}".format(board[4],board[5],board[6])) 
    print('    |   | ')
    print('-----------')
    print('    |   | ')
    print("  {0} | {1} | {2}".format(board[1],board[2],board[3]))
    print('    |   | ')
print("welcome to tic tac toe")
print("rules!")
print("follow number pattern accorinding to keyapad's right side number pad")
print(" 7    8    9")
print(" 4    5    6")
print(" 1    2    3")

#function for taking input.
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
#function for placing marker.
def place_marker(board, marker, position):
    board[position]=marker
#function for checking for winner.
def win_check(board, mark):
    return (board[1]==mark and board[3]==mark and board[2]==mark ) or (board[4]==mark and board[5]==mark and board[6]==mark ) or (board[7]==mark and board[8]==mark and board[9]==mark ) or (board[1]==mark and board[4]==mark and board[7]==mark ) or (board[2]==mark and board[5]==mark and board[8]==mark ) or (board[3]==mark and board[6]==mark and board[9]==mark ) or (board[1]==mark and board[5]==mark and board[9]==mark ) or (board[3]==mark and board[5]==mark and board[7]==mark ) 

#function for selecting first player.
def choose_first():
    if random.randint(0,1)==1:
        return 'player1'
    else:
        return 'player2'

#function for checking the poisition is empty or not

def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        return False
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board,turn):
    pos = 0
    
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board, pos):
        pos = int(input('{0}Choose your next position: (1-9) '.format(turn)))
        
    return pos
def replay():
    
    if input("enter yes to play again ").lower()[0]=='y':
        return True
    else:
        return False
while True :
    board=['_',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    p1_m,p2_m=player_input()
    turn=choose_first()
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn =='player1':
           
            display_board(board)
            pos=player_choice(board,turn)
            place_marker(board,p1_m,pos)
            if win_check(board,p1_m):
                display_board(board)
                print("player 1 has won the game")
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("the game is draw")
                    break
                else:
                    turn = 'player2'
        else:
            display_board(board)
            pos=player_choice(board,turn)
            place_marker(board,p2_m,pos)
            if win_check(board,p2_m):
                display_board(board)
                print("player 2 has won the game")
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("the game is draw")
                    break
                else:
                    turn = 'player1'
                
               
    if not replay():
            break
 
            
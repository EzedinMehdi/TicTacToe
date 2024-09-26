from random import randint
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]


def isChecked():
    pass
    

def mark(player):
    if player == 1:
        board[0][0] = 'X'
    elif player == 2:
        board[0][1] = 'X'
    elif player == 3:
        board[0][2] = 'X'
    elif player == 4:
        board[1][0] = 'X'
    elif player == 5:
        board[1][1] = 'X'
    elif player == 6:
        board[1][2] = 'X'
    elif player == 7:
        board[2][0] = 'X'
    elif player == 8:
        board[2][1] = 'X'
    elif player == 9:
        board[2][2] = 'X'
    else:
        print("Only enter 1-9")

def mark2(computer):
    if computer == 1:
        board[0][0] = 'O'
    elif computer == 2:
        board[0][1] = 'O'
    elif computer == 3:
        board[0][2] = 'O'
    elif computer == 4:
        board[1][0] = 'O'
    elif computer == 5:
        board[1][1] = 'O'
    elif computer == 6:
        board[1][2] = 'O'
    elif computer == 7:
        board[2][0] = 'O'
    elif computer == 8:
        board[2][1] = 'O'
    elif computer == 9:
        board[2][2] = 'O'
    else:
        print('only enter 1-9')


def gameOver():
    if board[0][0] == board[0][1] == board[0][2]:
        return False
    elif board[1][0] == board[1][1] == board[1][2]:
        return False
    elif board[2][0] == board[2][1] == board[2][2]:
        return False
    elif board[0][0] == board[1][0] == board[2][0]:
        return False
    elif board[0][1] == board[1][1] == board[2][1]:
        return False
    elif board[0][2] == board[1][2] == board[2][2]:
        return False
    elif board[0][0] == board[1][1] == board[2][2]:
        return False
    elif board[0][2] == board[1][1] == board[2][0]:
        return False
    else:
        return True


def print_board():
    for i in range(3):
        print(board[i])

while True:
        print_board()
        player1 = int(input("player X enter your move: "))
        mark(player1)
        print_board()
        
        if board[0][0] == board[0][1] == board[0][2]:
            print("Player X wins!!!")
            break
        elif board[1][0] == board[1][1] == board[1][2]:
            
            print("Player X wins!!!")
            break
        elif board[2][0] == board[2][1] == board[2][2]:
            
            print("Player X wins!!!")
            break
        elif board[0][0] == board[1][0] == board[2][0]:
            
            print("Player X wins!!!")
            break
        elif board[0][1] == board[1][1] == board[2][1]:
            
            print("Player X wins!!!")
            break
        elif board[0][2] == board[1][2] == board[2][2]:
            
            print("Player X wins!!!")
            break
        elif board[0][0] == board[1][1] == board[2][2]:
            
            print("Player X wins!!!")
            break
        elif board[0][2] == board[1][1] == board[2][0]:
            
            print("Player X wins!!!")
            break
        player2 = int(input("player O enter your move: "))
        mark2(player2)

        if board[0][0] == board[0][1] == board[0][2]:
            print("Player O wins!!!")
            break
        elif board[1][0] == board[1][1] == board[1][2]:
            
            print("Player O wins!!!")
            break
        elif board[2][0] == board[2][1] == board[2][2]:
            
            print("Player O wins!!!")
            break
        elif board[0][0] == board[1][0] == board[2][0]:
            
            print("Player O wins!!!")
            break
        elif board[0][1] == board[1][1] == board[2][1]:
            
            print("Player O wins!!!")
            break
        elif board[0][2] == board[1][2] == board[2][2]:
            
            print("Player O wins!!!")
            break
        elif board[0][0] == board[1][1] == board[2][2]:
            
            print("Player O wins!!!")
            break
        elif board[0][2] == board[1][1] == board[2][0]:
            
            print("Player O wins!!!")
            break
            
    
    # computer = randint(1, 9)
    # mark2(computer)


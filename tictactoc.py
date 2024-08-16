def sum_states(a, b, c):
    return a + b + c

def playgame(xstate, ystate):
    """Display the current state of the game board."""
    board = ['X' if xstate[i] else ('O' if ystate[i] else str(i)) for i in range(9)]
    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def checkwin(xstate, ystate):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    
    for win in wins:
        if sum_states(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            return 1
        if sum_states(ystate[win[0]], ystate[win[1]], ystate[win[2]]) == 3:
            return 0
    return -1

def is_draw(xstate, ystate):
    """Check if the game is a draw."""
    return all(xstate[i] or ystate[i] for i in range(9))

if __name__ == "__main__":
    xstate = [0] * 9
    ystate = [0] * 9
    turn = 1
    print("Welcome to the Tic Tac Toe game!")
    
    p1 = input("Enter First player name (sign X): ")
    p2 = input("Enter Second player name (sign O): ")
    
    while True:
        playgame(xstate, ystate)
        
        if turn == 1:
            print(f"{p1} X's turn")
        else:
            print(f"{p2} O's turn")
        
        value = int(input("Enter the position (0-8): "))
        
        if xstate[value] == 0 and ystate[value] == 0:
            if turn == 1:
                xstate[value] = 1
            else:
                ystate[value] = 1
        else:
            print("Position already taken. Try again.")
            continue
        
        winner = checkwin(xstate, ystate)
        if winner != -1:
            playgame(xstate, ystate)
            if winner == 1:
                print(f"{p1} has won!")
            else:
                print(f"{p2} has won!")
            break
        
        if is_draw(xstate, ystate):
            playgame(xstate, ystate)
            print("The game is a draw!")
            break
        
        turn = 1 - turn

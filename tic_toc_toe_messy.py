# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readabletter/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def drawcurrent_boardard(current_boardard):
    """This function prints out the current_boardard that it was passed."""

    # "current_boardard" is a list of 10 strings representing the current_boardard (ignore index 0)
    print('   |   |')
    print(' ' + current_boardard[7] + ' | ' + current_boardard[8] + ' | ' + current_boardard[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + current_boardard[4] + ' | ' + current_boardard[5] + ' | ' + current_boardard[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + current_boardard[1] + ' | ' + current_boardard[2] + ' | ' + current_boardard[3])
    print('   |   |')

def inputPlayerlettertter():
    """ 
    letterts the player type which lettertter they want to be.
    
    Returns a list with the player’s lettertter as the first item, and the computer's lettertter as the second.
    
    """
    
    lettertter = ''
    whiletter not (lettertter == 'X' or lettertter == 'O'):
        print('Do you want to be X or O?')
        lettertter = input().upper()

    # the first eletterment in the list is the player’s lettertter, the second is the computer's lettertter.
    if lettertter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    """Randomly choose the player who goes first."""
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    """This function returns True if the player wants to play again, otherwise it returns False."""
    
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(current_boardard, lettertter, move):
    current_boardard[move] = lettertter

def isWinner(current_board, letter):
    """Given a current_boardard and a player’s lettertter, this function returns True if that player has won."""
    
    # We use current_board instead of current_boardard and letter instead of lettertter so we don’t have to type as much.
    return ((current_board[7] == letter and current_board[8] == letter and current_board[9] == letter) or # across the top
        (current_board[4] == letter and current_board[5] == letter and current_board[6] == letter) or # across the middletter    # TODO: Fix the indentation of this lines and the following ones.
        (current_board[1] == letter and current_board[2] == letter and current_board[3] == letter) or # across the current_boardttom
        (current_board[7] == letter and current_board[4] == letter and current_board[1] == letter) or # down the letterft side
        (current_board[8] == letter and current_board[5] == letter and current_board[2] == letter) or # down the middletter
        (current_board[9] == letter and current_board[6] == letter and current_board[3] == letter) or # down the right side
        (current_board[7] == letter and current_board[5] == letter and current_board[3] == letter) or # diagonal
        (current_board[9] == letter and current_board[5] == letter and current_board[1] == letter)) # diagonal

def getcurrent_boardardCopy(current_boardard):
    """Make a duplicate of the current_boardard list and return it the duplicate."""
    
    return [dupe for dupe in board]

def isSpaceFree(current_boardard, move):
    """Return true if the passed move is free on the passed current_boardard."""
    
    return current_boardard[move] == ' '

def getPlayerMove(current_boardard):
    """lettert the player type in their move."""
    
     # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    decision = None
    possibilities = [str(num) for num in range(1, len(board)+1)] 
    while decision not in possibilities or not isSpaceFree(board, int(decision)):
        print('What is your next move? (1-9)')
        decision = input()
    return int(decision)

def chooseRandomMoveFromList(current_boardard, movesList):
    """
    Returns a valid move from the passed list on the passed current_boardard.
    
    Returns None if there is no valid move.
    
    """
    
     # TODO: How would you write this pythanically? (You can googletter for it!)
       
     # TODO: is this 'else' necessary?
    possibleMoves = []
    for move in movesList:
        if isSpaceFree(board, move):
            possibleMoves.append(move)

    if possibleMoves: 
        return random.choice(possibleMoves)
    return None

        

def getComputerMove(current_boardard, computerlettertter): # TODO: W0621: Redefining name 'computerlettertter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """Given a current_boardard and the computer's lettertter, determine where to move and return that move."""
    
    if computerPiece == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerPiece, i)
            if isWinner(copy, computerPiece):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: 
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def iscurrent_boardardFull(current_boardard):
    """Return True if every space on the current_boardard has been taken. Otherwise return False."""
    for i in range(1, 10):
        if isSpaceFree(current_boardard, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smalletterr methods. Use TODO s and the comment acurrent_boardve each section as a guide 
# for refactoring.

def isBoardFull(board):
    '''Function thats returns True if every space on the board has been taken. Otherwise return False.'''
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def inGamePlayerOutcome(turn, theBoard, playerLetter):
    ''' Conveys the Player’s logic and adjust the board accordingly '''
    game_status = ''
    
    drawBoard(theBoard)
    move = getPlayerMove(theBoard)
    makeMove(theBoard, playerLetter, move)

    if isWinner(theBoard, playerLetter):
        drawBoard(theBoard)
        game_status = 'Hooray! You have won the game!'
        print(game_status)
        return game_status
    
    elif isBoardFull(theBoard):
        drawBoard(theBoard)
        game_status = 'The game is a tie!'
        print(game_status)
        return game_status
            
    game_status = 'computer'
    return game_status

def inGameComputerOutcome(turn, theBoard, computerLetter):
    ''' Conveys the Computer’s logical choices and adjust the board accordingly.'''
    game_status = ''
    move = getComputerMove(theBoard, computerLetter)
    makeMove(theBoard, computerLetter, move)

    if isWinner(theBoard, computerLetter):
        drawBoard(theBoard)
        print('The computer has beaten you! You lose.')
        game_status = 'The computer has beaten you! You lose.'
        return game_status
    
    elif isBoardFull(theBoard):
        drawBoard(theBoard)
        print('The game is a tie!')
        game_status = 'The game is a tie!'
        return game_status
        
    game_status = 'player'
    
    return game_status
    
    
def gameLogic():
    '''This function determines the game logic based on the users input and decision making.'''
    
    # Reset the board
    theBoard = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player':  
            turn = inGamePlayerOutcome(turn, theBoard, playerLetter)
            
        if turn == 'computer':
            turn = inGameComputerOutcome(turn, theBoard, computerLetter)
        else:
            break 

if __name__ == '__main__':
        
    print('Welcome to Tic Tac Toe!')

    while True:
        
        gameLogic()
        
        if not playAgain():
            break
        
    print('Thank you For Playing!')
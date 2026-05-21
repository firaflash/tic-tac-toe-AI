
EMPTY = '___'
HUMAN = '_X_'
AI = '_O_'
arr = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

def printBoard():
    for t in range(12):
        print('_',end='')
    print()        
    
    for row in arr:
        print('|'.join(row))

def checkPos(x, y):
    return arr[x][y] != EMPTY

def check_input(row, col):
    return 0 <= row <= 2 and 0 <= col <= 2

def receive_input():
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if not check_input(row, col):
                print("Numbers must be between 0 and 2\n")
                continue
            if checkPos(row, col):
                print("Position already occupied\n")
                continue
            return row, col
        except ValueError:
            print("Enter valid whole numbers\n")

def handleInput():
    row, col = receive_input()
    arr[row][col] = HUMAN

def avalMoves():
    moves = []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == EMPTY:
                moves.append((i, j))
    return moves

def checkWiner():
    for row in arr:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if arr[0][col] == arr[1][col] == arr[2][col] != EMPTY:
            return arr[0][col]
    if arr[0][0] == arr[1][1] == arr[2][2] != EMPTY:
        return arr[0][0]
    if arr[0][2] == arr[1][1] == arr[2][0] != EMPTY:
        return arr[0][2]
    return None

def isDraw():
    return len(avalMoves()) == 0 and checkWiner() is None

def minmaxAlphaBeta(isAi, alpha, beta):
    winner = checkWiner()
    if winner == AI:
        return 10
    if winner == HUMAN:
        return -10
    if isDraw():
        return 0
    
    if isAi:
        best_score = float('-inf')
        for move in avalMoves():
            arr[move[0]][move[1]] = AI
            score = minmaxAlphaBeta(False, alpha, beta)
            arr[move[0]][move[1]] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in avalMoves():
            arr[move[0]][move[1]] = HUMAN
            score = minmaxAlphaBeta(True, alpha, beta)
            arr[move[0]][move[1]] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def best_move():
    best_score = float('-inf')
    best_move_pos = None
    alpha = float('-inf')
    beta = float('inf')
    
    for move in avalMoves():
        arr[move[0]][move[1]] = AI
        score = minmaxAlphaBeta(False, alpha, beta)
        arr[move[0]][move[1]] = EMPTY
        
        if score > best_score:
            best_score = score
            best_move_pos = move
        
        alpha = max(alpha, best_score)
    
    return best_move_pos

def ai():
    move = best_move()
    if move:
        arr[move[0]][move[1]] = AI

def playGame():
    current_turn = HUMAN
    while True:
        printBoard()
        if current_turn == HUMAN:
            print("Your Turn")
            handleInput()
        else:
            print("AI Thinking...")
            ai()
        
        winner = checkWiner()
        if winner == HUMAN:
            printBoard()
            print("HUMAN WINS")
            break
        if winner == AI:
            printBoard()
            print("AI WINS")
            break
        if isDraw():
            printBoard()
            print("DRAW")
            break
        
        if current_turn == HUMAN:
            current_turn = AI
        else:
            current_turn = HUMAN

if __name__ == "__main__":
    print("TIC TAC TOE")
    playGame()
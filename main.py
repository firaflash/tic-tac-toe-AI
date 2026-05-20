arr =  [['____','___','___'],
        ['____','___','___'],
        ['____','___','___']]
EMPTY = '___'
def printBoard():
    for t in range(12):
        print('_',end='')
    print()        
    
    for row in arr:
        print('|'.join(row))

def handleInput(): 
    val = receive_input()
    if isinstance(val, tuple) and len(val) == 2:
        arr[val[0]][val[1]] = '_X_'  
        return True
    return False

def checkPos(x,y):
    if arr[x][y] != '___':
        return True
    return False 
def avalMoves():
    board = []
    for i in range(3):
        for val in range(3):
            if arr[i][val] == '___':
                board.append([i,val])

    return board
def checkWiner():
    # rows
    for row in arr:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # columns
    for col in range(3):
        if arr[0][col] == arr[1][col] == arr[2][col] != EMPTY:
            return arr[0][col]

    # diagonals
    if arr[0][0] == arr[1][1] == arr[2][2] != EMPTY:
        return arr[0][0]

    if arr[0][2] == arr[1][1] == arr[2][0] != EMPTY:
        return arr[0][2]

    # no winner
    return None

def minmax(isAi):
    winner = checkWiner()
    if winner == '_X_':
        return 10
    if winner == '_O_':
        return -10
    if not winner:
        return 0
    if isAi:
        best_score = float('-inf')
        for i in avalMoves():
            arr[i[0],i[1]] = '_O_'
            score = minmax(False)
            arr[i[0],i[1]] = '___'
            best_score = max(best_score,score)            

            return best_score
    if not isAi:
        best_score = float('inf')
        for i in avalMoves():
            arr[i[0],i[1]]= '_X_'
            score = minmax(True)
            arr[i[0],i[1]]='___'
            best_score = min(best_score,score)
        return best_score
 






def best_move():
    best_score = float('-inf')
    best_move_pos = None
    for move in avalMoves():
        arr[move[0]][move[1]] = '_O_'
        move_score = minmax(True)
        arr[move[0]][move[1]] = " "
        if move_score > best_score:
            best_score = move_score
            best_move_pos = move
    return best_move_pos

def receive_input():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the col (0-2): "))
            
            if check_input(row, col):
                if(not checkPos(row,col)):
                    return row, col 
                print("Position already occupied")
            else:
                print("❌ Please enter numbers between 0 and 2.\n")
                
        except ValueError:
            print("❌ Invalid input. Please enter whole numbers only.\n")

def check_input(row, col):
    return 0 <= row <= 2 and 0 <= col <= 2
def ai():
    movs =  best_move()
    arr[movs[0]][movs[1]]='_O_'



def playGame():
    playing = True
    turn =  True
    while (playing):
        if(turn):
            bol = handleInput()
            turn=False
        ai()
        turn=True
        if(not bol):
           playing = False
           
        printBoard()


        


if __name__ == "__main__":
    printBoard()
    playGame()

arr = [['____','___','___'],
        ['____','___','___'],
        ['____','___','___']]
def printBoard():
    for row in arr:
        print(' | '.join(row))
        print('-' * 9)

def handleInput():  # Pass the board explicitly
    val = receive_input()
    if isinstance(val, tuple) and len(val) == 2:
        arr[val[0]][val[1]] = '_X_'  # ← Double brackets for lists
        return True
    return False


def receive_input():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the col (0-2): "))
            
            if check_input(row, col):
                
                return row, col 
            else:
                print("❌ Please enter numbers between 0 and 2.\n")
                
        except ValueError:
            print("❌ Invalid input. Please enter whole numbers only.\n")

def check_input(row, col):
    return 0 <= row <= 2 and 0 <= col <= 2

def playGame():
    playing = True
    while (playing):
        bol = handleInput()
        if(not bol):
           playing = False
           
        printBoard()


        


if __name__ == "__main__":
    printBoard()
    playGame()

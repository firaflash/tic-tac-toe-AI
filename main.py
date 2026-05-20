def printBord():
    arr = [['_n__','___','_x_'],
           ['_o__','___','___'],
           ['_x_','___','___']]
    br = [ "| "," | " , " | "," |"]
    # for t in range(11):
    #     print('_',end='')
    for row in range(3):
        for t in range(13):
            print('_',end='')
        print()
        print(' '.join(br))
        # for val in arr[row]:
        #     print('|'.join(arr))    
    for t in range(13):
            print('_',end='')
    print()


if __name__ == "__main__":
    printBord()
    

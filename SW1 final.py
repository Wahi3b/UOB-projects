def who_is_winner(pieces_position_list):
    
    board = [['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','','']]
    
    def updateBoard(board,column,turn):
        for i in range(6):
            if board[i][column] == '':
                board[i][column] = turn
                return board
            # elif i == 5 and board[i][column - 1] != '':
            #     return False
            # else:
            #     continue
    def gameDone(board):
        
        #Check Horizontal
        for i in range(6):
            for j in range(4):
                if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2] and board[i][j+2] == board[i][j+3] and board[i][j] != '':
                    results = board[i][j]
                    return results
        #Check Vertical
        for j in range(7):
            for i in range(3):
                if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j] and board[i+2][j] == board[i+3][j] and board[i+3][j] != '':
                    results = board[i][j]
                    return results
        #Check Diagonal
        for i in range(3):
            for j in range(3):
                if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] !='':
                    results = board[i][j]
                    return results
        for i in range(3):
            for j in range(1,4):
                if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] !='':
                    results = board[i][j]
                    return results
        for i in range(2):
            for j in range(2,4):
                if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] != '':
                    results = board[i][j]
                    return results
        for i in range(1,3):
            for j in range(2):
                if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] !='':
                    results = board[i][j]
                    return results
        
        for i in range(5,2,-1):
            for j in range(3):
                if board[i][j] == board[i-1][j+1] and board[i-1][j+1] == board[i-2][j+2] and board[i-2][j+2] == board[i-3][j+3] and board[i-3][j+3] !='':
                    results = board[i][j]
                    return results
        for i in range(4,2,-1):
            for j in range(2):
                if board[i][j] == board[i-1][j+1] and board[i-1][j+1] == board[i-2][j+2] and board[i-2][j+2] == board[i-3][j+3] and board[i-3][j+3] !='':
                    results = board[i][j]
                    return results
        for i in range(5,2,-1):
            for j in range(1,4):
                if board[i][j] == board[i-1][j+1] and board[i-1][j+1] == board[i-2][j+2] and board[i-2][j+2] == board[i-3][j+3] and board[i-3][j+3] !='':
                    results = board[i][j]
                    return results
        for i in range(5,3,-1):
            for j in range(2,4):
                if board[i][j] == board[i-1][j+1] and board[i-1][j+1] == board[i-2][j+2] and board[i-2][j+2] == board[i-3][j+3] and board[i-3][j+3] !='':
                    results = board[i][j]
                    return results
        i=2 
        j=0
        if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] != '':
                    results = board[i][j]
                    return results
        i=0
        j=3
        if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] != '':
                    results = board[i][j]
                    return results
        i=5
        j=3
        if board[i][j] == board[i-1][j+1] and board[i-1][j+1] == board[i-2][j+2] and board[i-2][j+2] == board[i-3][j+3] and board[i-3][j+3] !='':
                    results = board[i][j]
                    return results
        
        i=3
        j=0
        if board[i][j] == board[i-1][j+1] and board[i-1][j+1] == board[i-2][j+2] and board[i-2][j+2] == board[i-3][j+3] and board[i-3][j+3] !='':
                    results = board[i][j]
                    return results
        

        results = 'Draw'
        return results

    myDic ={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
    for item in pieces_position_list:
        entryList = item.split('_')
        column = myDic[entryList[0]]
        turn = entryList[1]
        board = updateBoard(board,column,turn)
        doneOrNot = gameDone(board)
        if doneOrNot == "Red" or doneOrNot == 'Yellow':
            break
    return doneOrNot        
    
    
    

        

         




who_is_winner([
"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", 
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", 
"B_Yellow", "B_Red"
])
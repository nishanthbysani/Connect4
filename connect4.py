ROW_COUNT = 6
COL_COUNT =7
def create_board():
    board = [ [ 0 for i in range(COL_COUNT) ] for j in range(ROW_COUNT) ]
    #a[0][0] = 5
    # for i in range(ROW_COUNT):
    #     for j in range(COL_COUNT):
    #         print(board[i][j] , end =" ")
    #     print("")
    for row in range(ROW_COUNT):
       print(board[row])
    return board     

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r

def print_board(board):
    # for j in range(COL_COUNT):
    #     for i in range(ROW_COUNT):
    #         print("Before  row =",i,"Col=",j , "i ,j =",i,j ,"[i][j] ",board[i][j] ,"ROW_COUNT-i-1=",ROW_COUNT-i-1, board[ROW_COUNT-i-1][j])
    #         board[i][j] , board[ROW_COUNT-i-1][j] =  board[ROW_COUNT-i-1][j] , board[i][j]
    #         print("After  row =",i,"Col=",j , "i ,j =",board[i][j] ,"[i][j] ",board[i][j] ,"ROW_COUNT-i-1=",ROW_COUNT-i-1, board[ROW_COUNT-i-1][j])          

   for row in reversed(range(ROW_COUNT)):
       print(board[row])


# Calculating the scores
def scores_calculator(board,piece):
    score =0
    #Horizontal Win
    for rows in range(ROW_COUNT):
        for cols in range(COL_COUNT-3):
            if board[rows][cols] == piece and board[rows][cols+1] == piece and board[rows][cols+2] == piece and board[rows][cols+3] == piece:
                score+=1
    #Vertical Win
    for cols in range(COL_COUNT):
        for rows in range(ROW_COUNT-3):
            if board[rows][cols] == piece and board[rows+1][cols] == piece and board[rows+2][cols] == piece and board[rows+3][cols] == piece:
                score += 1
    #Positvely Sloped Diagonal
    for cols in range(COL_COUNT-3):
        for rows in range(ROW_COUNT-3):
            if board[rows][cols] == piece and board[rows+1][cols+1] == piece and board[rows+2][cols+2] == piece and board[rows+3][cols+3] == piece:
                score += 1
    #Negatively Sloped Diagonal
    for cols in range(COL_COUNT-3):
        for rows in range(3,ROW_COUNT):
            if board[rows][cols] == piece and board[rows-1][cols+1] == piece and board[rows-2][cols+2] == piece and board[rows-3][cols+3] == piece:
                score += 1
    return score

board = create_board()
game_over = False
turn =0
while not game_over:
    #Ask for Player 1 Input
    if turn==0:
        col= int(input("Player 1  Makes a selection (0-6)"))
        if col not in range(7):
            print("Enter column number between 0 to 6")
            continue
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,1)
            print_board(board)
            if scores_calculator(board,1):
                print("Player 1 wins")
                game_over = True

    #Ask for Player 2 Input
    else:
        col= int(input("Player 2  Makes a selection (0-6)"))
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,2)
            print_board(board)

    turn += 1
    turn = turn % 2
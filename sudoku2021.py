import time

mainboard = [
[0,0,0,9,4,5,0,0,0],
[7,6,5,0,0,0,0,9,0],
[0,9,0,0,0,0,0,3,0],
[9,0,0,0,0,4,0,0,0],
[6,0,0,8,9,2,0,0,3],
[0,0,0,3,0,0,0,0,2],
[0,2,0,0,0,0,0,1,0],
[0,1,0,0,0,0,7,8,4],
[0,0,0,5,1,7,0,0,0]
]

def column_build(board):
    total_columns = []
    for j in range(9):
        column = []
        for i in range(9):
            column.append(board[i][j])
        total_columns.append(column)
    return total_columns

def square_build(board):
    square = []
    for column in range(3):
        for row in range(3):
            square.append([board[item][row*3:row*3+3] for item in range(column*3,column*3+3)])
            square[-1] = square[-1][-3] + square[-1][-2] + square[-1][-1]
    return square


def squarefind(spot: list[int, int]) -> int:
    squarenum = 0
    for row in range(3):
        for column in range(3):
            if spot[0] >= row * 3 and spot[0] < row * 3 + 3 and spot[1] >= column *3 and spot[1] < column *3 + 3:
                return squarenum
            squarenum += 1
    return squarenum

def candidatefind(board, spot: list[int, int], candidate) -> bool:
    colboard = column_build(board)
    squareboard = square_build(board)

    squareindex = squarefind(spot)

    if candidate not in board[spot[0]] and candidate not in colboard[spot[1]] and candidate not in  squareboard[squareindex]:
        return True
    else:
        return False

def printer(board):
    print('\n _ _ _ _ _ _ _ _ _ ')
    for i in range(9):
        print('|', end="")
        for j in range(9):
            print(f'{board[i][j]}|', end="")
        print('\n _ _ _ _ _ _ _ _ _ ')
    print("\n")

def checkdone(board):
    unfilled = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                unfilled += 1

    return unfilled

undone = 0
def solver(board):
    global undone
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: 
                for item in range(1,10):
                    candidate = candidatefind(board, [row, col], item)
                    if candidate == True:
                        undone+=1
                        board[row][col] = item
                        #print(row, col)
                        if checkdone(board) == 0:
                            print(f'Board solved after {undone} trials.')
                            printer(board)
                            exit()

                        #print(f'{checkdone(board)} left')
                        solver(board)
                        board[row][col] = 0

                return board

print("""\nWelcome to sudoku. 
I can solve any sudoku puzzle out there. \n
Initial Board: """)
printer(mainboard)
test = solver(mainboard)
printer(test)
# printer(column_build(mainboard))
# printer(square_build(mainboard))
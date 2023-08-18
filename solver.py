N = 9
cnt = 0

# sudoku[N][N]

def isSafe(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    for i in range(9):
        if sudoku[i][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    return True


def solveSudoku(sudoku, row, col):
    global cnt
    cnt += 1

    if cnt > 1000:
        return False


    if row == N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1)

    for num in range(1, N + 1):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num

            if solveSudoku(sudoku, row, col + 1):
                return True
        sudoku[row][col] = 0
    return False


def solver(sudoku):
    global cnt
    if solveSudoku(sudoku, 0, 0):
        cnt = 0
        return sudoku
    else:
        cnt = 0
        return "no"

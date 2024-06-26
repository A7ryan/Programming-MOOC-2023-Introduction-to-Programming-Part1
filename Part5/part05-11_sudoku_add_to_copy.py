def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    x = [row.copy() for row in sudoku]
    x[row_no][column_no] = number
    return x

def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = "_"
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=' ')
            if (j+1) % 3 == 0:
                print(end=' ')
        print()
        if i > 0 and (i+1) % 3 == 0:
            print()


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

def block_correct(sudoku: list, row_no: int, column_no: int):
    l = []
    for i in range(3):
        for j in range(3):
            if sudoku[row_no][column_no+j] != 0:
                l.append(sudoku[row_no][column_no+j])
        row_no += 1
    l = sorted(l)
    m = sorted(list(set(l)))
    return True if l == m else False

    
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 3))
    print(block_correct(sudoku, 1, 2))

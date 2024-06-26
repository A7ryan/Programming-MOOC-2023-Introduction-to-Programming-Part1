def row_correct(sudoku: list, row_no: int):
    l = sorted(sudoku[row_no])
    temp = []
    for i in range(len(l)):
        if l[i] == 0:
            temp = temp
        else:
            temp.append(l[i])
    s = set(temp)
    return True if sorted(s) == temp else False

def column_correct(sudoku: list, column_no: int):
    l = []
    temp = []
    for i in range(len(sudoku)):
        l.append(sudoku[i][column_no])
    l = sorted(l)
    for i in range(len(l)):
        if l[i] == 0:
            temp = temp
        else:
            temp.append(l[i])
    s = sorted(list(set(temp)))
    return True if s == temp else False

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


def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True


if __name__ == "__main__":
    sudoku = [
    [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
    [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
    [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
    [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
    [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
    [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
    [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
    [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
    [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    ]
    
    print(sudoku_grid_correct(sudoku))
        
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

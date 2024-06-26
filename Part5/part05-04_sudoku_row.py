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
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))

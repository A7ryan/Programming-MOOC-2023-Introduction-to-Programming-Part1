def who_won(game_board: list):
    p1 = 0
    p2 = 0

    for i in game_board:
        for j in i:
            if j == 1:
                p1 += 1
            elif j == 2:
                p2 += 1
        
    return 1 if p1 > p2 else 2 if p2 > p1 else 0


if __name__ == "__main__":
    x = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(x))

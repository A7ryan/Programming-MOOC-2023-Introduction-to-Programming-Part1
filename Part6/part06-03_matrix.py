def list_total(x):
    t = 0
    for n in x:
        t += n
    return t

def matrix_sum():
    sum = 0
    with open("matrix.txt") as new_file:
        for i in new_file:
            temp = i.split(',')
            for j in temp:
                sum += int(j)
        return sum

def matrix_max():
    l = []
    with open("matrix.txt") as new_file:
        for i in new_file:
            temp = i.split(',')
            for j in temp:
                l.append(int(j))
        x = sorted(l)
        return x[-1]


def row_sums():
     with open("matrix.txt") as new_file:
        l = []
        for i in new_file:
            temp = i.split(',')
            n = []
            for i in temp:
                n.append(int(i))
            l.append(list_total(n))
        return l

if __name__ == '__main__':
    matrix_max()
    matrix_sum()
    row_sums()

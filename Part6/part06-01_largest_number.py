def largest():
    l = []
    with open("numbers.txt") as new_file:
        for i in new_file:
            l.append(int(i))
    x = sorted(l)
    return x[-1]


if __name__ == '__main__':
    largest()

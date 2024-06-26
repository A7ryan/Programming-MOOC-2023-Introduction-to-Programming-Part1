def list_of_stars(l):
    for i in range(len(l)):
        print("*"*l[i],end='')
        print()


if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])

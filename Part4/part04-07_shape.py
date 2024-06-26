def line(n,s):
    if s == "":
        print("*"*n)
    else:
        print(s[0]*n)


def shape(width,char1,height,char2):
    for i in range(width+1):
        line(width-(width-i),char1)
    for i in range(height):
        line(width,char2)


if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")

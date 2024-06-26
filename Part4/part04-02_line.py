def line(n,s):
    if s == "":
        print("*"*n)
    else:
        print(s[0]*n)

if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")

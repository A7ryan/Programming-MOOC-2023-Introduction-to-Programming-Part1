def line(n,s):
    if s == "":
        print("*"*n)
    else:
        print(s[0]*n)

def square(size, character):
    for i in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")

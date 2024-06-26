def line(n,s):
    if s == "":
        print("*"*n)
    else:
        print(s[0]*n)

def triangle(size):
    for i in range(size+1):
        line(size-(size-i), "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

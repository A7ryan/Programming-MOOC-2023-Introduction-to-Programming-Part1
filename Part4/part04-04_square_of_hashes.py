def line(n,s):
    if s == "":
        print("*"*n)
    else:
        print(s[0]*n)

def square_of_hashes(size):
    for i in range(size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

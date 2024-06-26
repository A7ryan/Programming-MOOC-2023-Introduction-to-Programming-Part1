def spruce(n):
    print()
    print("a spruce!")
    for i in range(1, n+1):
        print (" " *(n-i) + "*"*(2*i-1))
    print (" " * (n-1) + "*")

if __name__ == "__main__":
    spruce(3)

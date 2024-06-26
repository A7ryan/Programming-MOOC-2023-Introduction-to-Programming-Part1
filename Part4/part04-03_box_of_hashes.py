def line(n,s):
    if s == "":
        print("*"*n)
    else:
        print(s[0]*n)

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")
    

if __name__ == "__main__":
    box_of_hashes(5)

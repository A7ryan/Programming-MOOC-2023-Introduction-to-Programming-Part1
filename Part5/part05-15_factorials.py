def factorials(n: int):
    d = {1:1}
    for i in range(2,n+1):
        d[i] =  i * d[(i-1)]
    return d

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
    

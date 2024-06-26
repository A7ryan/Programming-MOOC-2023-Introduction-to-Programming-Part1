n = int(input("Please type in a postive integer: "))
l = [x for x in range(-n,n+1) if x != 0]
for i in l:
    print(i)

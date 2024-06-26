l = []
c = 0
while 1:
    s = input("Word: ")
    if not s in l:
        c = c+1
        l.append(s)
    else:
        print(f"You typed in {c} different words")
        break

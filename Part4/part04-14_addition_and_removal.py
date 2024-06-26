l = []

while 1:
    print("The list is now {0}".format(l))
    s = input("a(d)d, (r)emove or e(x)it: ")
    if s == 'd':
        if l == []:
            l.append(1)
        else:
            l.append(l[-1]+1)
    elif s == 'r':
        l.pop()
    elif s == 'x':
        print("Bye!")
        break

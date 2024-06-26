l = []
order_l = []

while 1:
    n = int(input("New item: "))
    if n == 0:
        print("Bye!")
        break
    else:
        l.append(n)
        print("The list now: {0}".format(l))
        order_l = sorted(l)
        print("The list in order: {0}".format(order_l))

l = []
how_many_items = int(input(("How many items: ")))
for i in range(1,how_many_items+1):
    l.append(int(input("Item {0}: ".format(i))))
print(l)

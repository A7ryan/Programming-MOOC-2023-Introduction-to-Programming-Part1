l = [1,2,3,4,5]

while 1:
    index = int(input("Index: "))
    if index == -1:
        break
    else:
        new_value = int(input("New value: "))
        l[index] = new_value
        print(l)

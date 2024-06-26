d = {}
command = 0

while 1:
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 1:
        name = input("name: ")
        if name in d:
            for i in d[name]:
                print(i)
        else:
            print("no number")
    
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in d:
            d[name] = []
        d[name].append(number)
        print("ok!")

    if command == 3:
        print("quitting...")
        break

        

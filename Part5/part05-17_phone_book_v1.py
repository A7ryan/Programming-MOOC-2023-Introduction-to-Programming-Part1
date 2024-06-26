d = {}
command = 0

while 1:
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 1:
        name = input("name: ")
        if name in d:
            print(d[name])
        else:
            print("no number")
    
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        d[name] = number
        print("ok!")

    if command == 3:
        print("quitting...")
        break

        

while 1:
    s = input("Editor: ")
    s = s.lower()
    if s == "word" or s == "notepad":
        print("awful")
    elif s == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")

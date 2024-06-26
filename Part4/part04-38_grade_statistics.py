l = []
zero = one = two = three = four = five = 0
sum = p = c = 0

while 1:
    s = input("Exam points and exercises completed: ")
    if s == "":
        avg = sum/c
        p = ((c - zero)*100)/c
        print("Statistics:")
        print(f"Points average: {avg}")
        print(f"Pass percentage: {p:.1f}")
        print("Grade distribution: ")
        for i in range(5,-1,-1):
            print("{0}: {1}".format(i,("*"*l[i])))
        break
    else:
        c += 1
        a,b = map(int, s.split(" "))
        b = int(b/10)
        sum += (a+b)
        if a < 10 or ((a+b) >= 0 and (a+b) <=14):
            zero += 1
        elif (a+b) >= 15 and (a+b) <=17:
            one += 1
        elif (a+b) >= 18 and (a+b) <=20:
            two += 1
        elif (a+b) >= 21 and (a+b) <=23:
            three += 1
        elif (a+b) >= 24 and (a+b) <= 27:
            four += 1
        elif (a+b) >= 28 and (a+b) <= 30:
            five += 1
    l = [zero,one,two,three,four,five]

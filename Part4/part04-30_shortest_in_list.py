def shortest(l):
    s = ""
    smallest_len = len(l[0])
    for i in range(len(l)-1):
        if len(l[i+1]) < smallest_len:
            smallest_len = len(l[i+1])
            s = l[i+1]
    if s == "":
        return l[0]
    else:
        return s        
       
if __name__ == "__main__":
    my_list = ['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']
    result = shortest(my_list)
    print(result)

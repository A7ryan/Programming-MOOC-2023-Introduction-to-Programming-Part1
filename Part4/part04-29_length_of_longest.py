def length_of_longest(l):
    size = len(l[0])
    for i in range(1,len(l)-1):
        if size < len(l[i+1]):
            size = len(l[i+1])
    return size

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

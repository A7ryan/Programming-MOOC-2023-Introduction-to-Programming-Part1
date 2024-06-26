def all_the_longest(l):
    temp = []
    size = len(l[0])
    for i in range(1,len(l)-1):
        if size < len(l[i+1]):
            size = len(l[i+1])
    for i in range(len(l)):
        if len(l[i]) == size:
            temp.append(l[i])
    return temp

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']

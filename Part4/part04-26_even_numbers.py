def even_numbers(l):
    new = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            new.append(l[i])
    return new

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)

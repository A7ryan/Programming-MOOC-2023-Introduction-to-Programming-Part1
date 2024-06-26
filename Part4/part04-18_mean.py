def mean(l):
    sum = 0.0
    for i in range(len(l)):
        sum += (l[i])
    return sum/len(l)

if __name__ == "__main__":
    my_list = [1, 3, 67, 7, 4, 23, 1, 5, 7, 4]
    result = mean(my_list)
    print(result)

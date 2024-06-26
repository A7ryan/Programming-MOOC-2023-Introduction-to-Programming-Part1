def sum_of_positives(l):
    sum = 0
    for i in range(len(l)):
        if l[i] > 0:
            sum += l[i]
    return sum


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)

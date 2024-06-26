def longest_series_of_neighbours(l):
    c = 1
    temp = 0
    for i in range(len(l)-1):
        if abs(l[i] - l[i+1]) == 1:
            c += 1
        else:
            temp = max(temp,c)
            c = 1
    return max(temp,c)

if __name__ == "__main__":
    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))

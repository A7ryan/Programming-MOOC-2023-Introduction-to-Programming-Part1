def list_sum(l1,l2):
    sum = []
    for i in range(len(l1)):
        sum.append(l1[i] + l2[i])
    return sum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]

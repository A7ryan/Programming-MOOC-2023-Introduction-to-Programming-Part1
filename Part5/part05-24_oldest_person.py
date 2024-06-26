def oldest_person(people: list):
    temp_list = []
    for i in range(len(people)):
        temp_list.append(people[i][1])
    check_index = temp_list.index(min(temp_list))
    temp_value = people[check_index]
    return temp_value[0]

if __name__ == '__main__':
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))

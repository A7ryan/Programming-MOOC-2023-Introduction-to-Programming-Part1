def older_people(people: list, year: int):
    temp_list = []
    name = []
    for i in range(len(people)):
        if people[i][1] < year:
            temp_list.append(people[i])
    for p in temp_list:
        nme,yr = p
        name.append(nme)
    return name


if __name__ == '__main__':
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)

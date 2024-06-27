def read_fruits():
    d = {}
    with open("fruits.csv") as new_file:
        for i in new_file:
            key,value = i.split(';')
            d[key] = float(value)
    return d

if __name__ == '__main__':
    read_fruits

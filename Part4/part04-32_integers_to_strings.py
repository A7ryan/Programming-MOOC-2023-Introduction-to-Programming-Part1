def formatted(l):
    return [f'{x:.2f}' for x in l]

if __name__ == "__main":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)

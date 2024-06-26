def remove_smallest(numbers: list):
    x = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < x:
            x = numbers[i]
    return numbers.remove(x)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)

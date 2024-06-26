def longest(strings: list):
    #x = 0
    #temp = 0
    #for i in len(strings)-1:
    #    if len(strings[i]) < len(strings[i+1]):
    #        if len(strings[i+1]) > temp:
    #            x = strings[i+1]
    #        else:
    #            break
    #    else:
    #        x = x
    #    temp = len(x)
    #return x
    return max(strings, key = len)


if __name__ == "__main__":
    strings = ['ab', 'abcd', 'abc', 'acbdefg', 'a', 'abcd', 'aa']
    print(longest(strings))
    strings = ['orange', 'apple', 'milkshake', 'banana', 'pear']
    print(longest(strings))

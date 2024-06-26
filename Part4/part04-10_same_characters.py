def same_chars(s,i1,i2):
    try:
        if s[i1] == s[i2]:
            return True
        else:
            return False
    except IndexError:
        return False


if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False

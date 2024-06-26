def palindromes(s):
    l1 = list(s)
    l2 = list(reversed(s))
    return True if l1 == l2 else False


while 1:
    s = input("Please type in a palindrome: ")
    bool = palindromes(s)
    if bool == True:
        print(f"{s} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

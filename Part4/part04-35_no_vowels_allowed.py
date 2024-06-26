def no_vowels(s):
    temp = ""
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            temp += s[i].replace(s[i],"")
        else:
            temp += s[i]
    return temp

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

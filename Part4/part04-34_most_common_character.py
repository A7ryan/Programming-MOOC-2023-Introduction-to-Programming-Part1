def most_common_character(s):
    d = {}
    for i in s:
      if i in d:
        d[i] += 1
      else:
        d[i] = 1
    x = max(d,key=d.get)
    return x

if __name__ == "__main__":
    first_string = "aaabb"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))


#def most_common_character(string):
#    char_count = {}
#    for char in string:
#        char_count[char] = char_count.get(char, 0) + 1
#    
#    most_common = None
#    max_count = 0
#    for char, count in char_count.items():
#        if count > max_count or (count == max_count and char < most_common):
#            most_common = char
#            max_count = count
#    
#    return most_common

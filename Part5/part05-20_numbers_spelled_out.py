def dict_of_numbers():
    zero_to_nineteen = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
         11: 'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
         18:'eighteen',19:'nineteen'}
    
    greater_than_nineteen = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty',
                             9:'ninety'}
    
    spell_number = {}
    
    for i in range(100):
        if i < 20:
            spell_number[i] = zero_to_nineteen[i]
        else:
            check_tens_num = i // 10
            check_unit_num = i % 10
            spell_number[i] = greater_than_nineteen[check_tens_num]
            if check_unit_num > 0:
                spell_number[i] += "-" + zero_to_nineteen[check_unit_num]
            
    return spell_number           



if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])

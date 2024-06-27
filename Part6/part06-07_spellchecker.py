def fun():
    l = []
    with open('wordlist.txt') as new_file:
        for i in new_file:
            i = i.replace('\n','')
            l.append(i)        
        return l
        

def main():
    input_text = input('Enter text: ')
    txt = input_text.split(' ')
    new_dict = fun()
    output = ''
    for input_text in txt:
        if input_text.lower() in new_dict:
            output += input_text
        else:
            output += '*' + input_text + '*'
        output += ' '
    print(output)

main()

def everything_reversed(l):
    return [x[::-1] for x in reversed(l)]
    
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

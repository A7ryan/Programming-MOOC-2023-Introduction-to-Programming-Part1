def invert(dictionary: dict):
    d = {key:value for value,key in dictionary.items()}
    dictionary.clear()
    dictionary.update(d)
    
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

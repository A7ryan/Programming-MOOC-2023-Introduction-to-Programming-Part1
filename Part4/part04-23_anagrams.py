def anagrams(s1,s2):
    l1 = sorted(list(s1))
    l2 = sorted(list(s2))
    return True if l1 == l2 else False  

if __name__ == "__main":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False

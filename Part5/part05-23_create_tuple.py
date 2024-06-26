def create_tuple(x: int, y: int, z: int):
    t = (min(x,y,z),max(x,y,z),sum([x,y,z]))
    return t

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

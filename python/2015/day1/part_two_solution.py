def solution() -> int:
    with open("input.txt", "r") as f:
        f_contents = f.read()

    floor = 0
    pos = 0 # Pos is one indexed, so if zero, then floor was never < 0

    while not floor < 0:
        floor += 1 if f_contents[pos] == "(" else -1
        pos += 1
    return pos
    
print(solution()) # Prints 1771 
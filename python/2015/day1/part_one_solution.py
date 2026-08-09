def solution() -> int:
    with open("input.txt") as f:
        f_contents = f.read()

    floor = 0
    
    for char in f_contents:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor
    
print(solution()) # Prints 138
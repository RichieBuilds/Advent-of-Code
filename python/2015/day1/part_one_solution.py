def solution() -> int:
    with open("input.txt") as f:
        f_contents = f.read()

    floor = f_contents.count("(") - f_contents.count(")")
    
    return floor
    
print(solution()) # Prints 138
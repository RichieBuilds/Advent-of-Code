def solution() -> int | None:
    with open("input.txt", "r") as f:
        f_contents = f.read()

    floor = 0
    
    for i in range(len(f_contents)):
        if f_contents[i] == "(":
            floor += 1
        elif f_contents[i] == ")":
            floor -= 1
        if floor < 0:
            # Remember loop starts counting at 0. So we just add 1 to get the natural position of the number
            return i + 1     

print(solution()) # Prints 1771 
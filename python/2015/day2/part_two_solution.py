def solution() -> int:
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = line.split("x")
            l = int(line[0])
            w = int(line[1])
            h = int(line[2])

            total += volume(l, w, h) + min_prm(l, w, h)

    return total

# Volume of the present
def volume(l: int, w: int, h: int) -> int:
    return l * w * h

# Smallest perimeter
def min_prm(l: int, w: int, h: int) -> int:
    dimentions = [l, w, h]
    min_1 = min(dimentions)
    dimentions.remove(min_1)
    min_2 = min(dimentions)

    return (2 * min_1) + (2 * min_2)

print(solution()) # Prints 3783758
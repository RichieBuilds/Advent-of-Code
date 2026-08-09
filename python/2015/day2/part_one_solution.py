def solution() -> int:
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = line.split("x")
            l = int(line[0])
            w = int(line[1])
            h = int(line[2])

            total += sa(l, w, h) + min_sa(l, w, h)

    return total
            
# Surface Area for a rectangular cuboid
def sa(l: int, w: int, h:int) -> int:
    return (2 * l * w) + (2 * w * h) + (2 * h * l)

# Area for the smallest side
def min_sa(l: int, w: int, h:int) -> int:
    dimentions = [l, w, h]
    min_1 = min(dimentions)
    dimentions.remove(min_1)
    min_2 = min(dimentions)

    return min_1 * min_2

print(solution()) # Prints 1588178
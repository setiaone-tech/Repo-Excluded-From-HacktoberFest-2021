from sys import stdout, stdin
def interact(type, x):
    if type == "r":
        inp = input()
        return inp.strip()
    else:
        print(x, flush=True)

for _ in range(int(interact("r", 0))):
    for i in range(1, 1001):
        interact('w', i**2)
        if interact('r', 0) == "1":
            break


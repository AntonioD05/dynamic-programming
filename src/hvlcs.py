import sys
def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        char, val = lines[i].split()
        values[char] = int(val)

    A = lines[k + 1]
    B = lines[k + 2]

    return values, A, B

values, A, B = read_input(sys.argv[1])
print(values)
print(A)
print(B)
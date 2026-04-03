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

def compute_hvlcs(values, A, B):
    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

            if A[i] == B[j]:
                dp[i][j] = max(dp[i][j], values[A[i]] + dp[i + 1][j + 1])

    subsequence = []
    i, j = 0, 0

    while i < n and j < m:
        if A[i] == B[j] and dp[i][j] == values[A[i]] + dp[i + 1][j + 1]:
            subsequence.append(A[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return dp[0][0], "".join(subsequence)

def main():
    filename = sys.argv[1]
    values, A, B = read_input(filename)
    max_value, subsequence = compute_hvlcs(values, A, B)

    print(max_value)
    print(subsequence)

if __name__ == "__main__":
    main()
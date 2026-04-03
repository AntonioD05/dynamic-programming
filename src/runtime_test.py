import time
import matplotlib.pyplot as plt
from hvlcs import read_input, compute_hvlcs

files = [
    "data/test1.in",
    "data/test2.in",
    "data/test3.in",
    "data/test4.in",
    "data/test5.in",
    "data/test6.in",
    "data/test7.in",
    "data/test8.in",
    "data/test9.in",
    "data/test10.in",
]

sizes = []
times = []

for filename in files:
    values, A, B = read_input(filename)

    start = time.perf_counter()
    max_value, subsequence = compute_hvlcs(values, A, B)
    end = time.perf_counter()

    runtime = end - start
    size = len(A) * len(B)

    sizes.append(size)
    times.append(runtime)

    print(f"{filename}: size={size}, time={runtime:.6f} seconds")

plt.plot(sizes, times, marker="o")
plt.xlabel("Input size (len(A) * len(B))")
plt.ylabel("Runtime (seconds)")
plt.title("HVLCS Runtime on 10 Input Files")
plt.grid(True)
plt.savefig("runtime_graph.png")
plt.show()
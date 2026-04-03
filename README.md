# Highest Value Longest Common Sequence

## Student Information
- Name: Antonio Diaz
- UFID: 73464639

## Repository Structure
- `src/` contains the Python source files:
  - `hvlcs.py` computes the highest value longest common subsequence for a given input file.
  - `runtime_test.py` runs the empirical runtime experiment on 10 test files and generates the runtime graph.
- `data/` contains the example input file and the 10 nontrivial test input files.
- `runtime_graph.png` contains the graph for Question 1.
- `README.md` contains instructions, assumptions, and written answers for Questions 1, 2, and 3.

## Build / Compile Instructions
No compilation is required for this project because it is implemented in Python.

## How to Run

To run the program on the example input:
```bash
python src/hvlcs.py data/example.in
```

To run the program on any of the other test files:

```bash
python src/hvlcs.py data/test1.in
python src/hvlcs.py data/test2.in
python src/hvlcs.py data/test3.in
python src/hvlcs.py data/test4.in
python src/hvlcs.py data/test5.in
python src/hvlcs.py data/test6.in
python src/hvlcs.py data/test7.in
python src/hvlcs.py data/test8.in
python src/hvlcs.py data/test9.in
python src/hvlcs.py data/test10.in
```

To run the empirical runtime comparison and generate the graph for Question 1:

```bash
python src/runtime_test.py
```

If `matplotlib` is not installed, install it with:

```bash
pip install matplotlib
```

## Example Input and Output

Example input file: `data/example.in`

```text
3
a 2
b 4
c 5
aacb
caab
```

Example command:

```bash
python src/hvlcs.py data/example.in
```

Expected output:

```text
9
cb
```

## Assumptions

* The input file follows the assignment format exactly.
* The first line contains the number of characters in the alphabet.
* The next `K` lines each contain one character and its assigned integer value.
* The final two lines contain the two input strings `A` and `B`.
* Character values are nonnegative integers.
* Blank lines in the input file are ignored by the parser.
* If multiple optimal subsequences exist, the program may output any one of them.
import math
import numpy as np
from collections import Counter

DEFAULT_INPUT_SIZE = "large"

def get_lines(input_size=None):
    with open("input."+input_size, "r") as f:
        lines = [int(l.strip()) for l in f.readlines()]
    return lines

def run(lines=None):
    ls = [0] + sorted(lines) 
    deltas = [ls[i+1]-ls[i] for i in range(len(ls)-1)] + [3]
    cnt = Counter(deltas)
    p1 = math.prod([x[1] for x in cnt.items()])
    # Part 2
    vec = np.array([1, 0, 0])
    lkp = {"1": np.array([[1,1,1],[1,0,0],[0,1,0]]),
           "2": np.array([[1,1,0],[0,0,0],[1,0,0]]),
           "3": np.array([[1,0,0],[0,0,0],[0,0,0]])}
    for d in deltas:
        vec = np.matmul(lkp[str(d)], vec)
    p2 = vec[0]
    return p1, p2

def main():
    lines = get_lines(input_size=DEFAULT_INPUT_SIZE)
    print(run(lines))

if __name__ == "__main__":
    main()

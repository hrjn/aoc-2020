import numpy as np
from collections import deque

def get_slider(data, size_preamble):
    return (list(data)[i:i+size_preamble+1] for i in range(len(data)-size_preamble))

def load_data(input_file):
    with open(input_file, "r") as f:
        return deque([int(x.strip()) for x in f.readlines()])

def run(input_file="input.txt", size_preamble=25):
    # Part 1
    data = load_data(input_file)
    slider = get_slider(data, size_preamble)
    for s in slider:
        sa = np.array(s[:-1])
        osum = set((sa[None,:] + sa[:,None]).reshape(1,size_preamble**2).tolist()[0])
        if s[-1] not in osum:
            part_1 = s[-1]
    # Part 2
    q = deque()
    while sum(q) <= part_1:
        if sum(q) == part_1:
            qs = sorted(q)
            part_2 = qs[0] + qs[-1]
            break
        else:
            q.append(data.popleft())
            while sum(q) > part_1:
                q.popleft()
    return part_1, part_2

def main():
    print(run())
if __name__ == "__main__":
    main()

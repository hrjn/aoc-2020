import numpy as np

def part_1(v, target_sum=2020):
    ind = np.where(np.add.outer(v,v)==target_sum)[0]
    out = v[ind]
    return int(np.prod(out))

def part_2(v, target_sum=2020):
    v_outsum = np.add.outer(v,v)
    for k in range(len(v)):
        v_outsum_3d = v_outsum + np.full(v_outsum.shape,v[k])
        ind = np.where(v_outsum_3d==target_sum)[0]
        if ind.size != 0:
            out = v[np.append(ind, k)]
    return int(np.prod(out))

def main():
    v = np.loadtxt("input.txt")
    print(f"Answer for part 1: {part_1(v)}")
    print(f"Answer for part 2: {part_2(v)}")

if __name__ == "__main__":
    main()

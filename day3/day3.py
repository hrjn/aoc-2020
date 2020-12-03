import math

def part_1(grid_file, tree_char, slope):
    cpt = 0
    with open(grid_file, 'r') as f:
        lines = f.read().splitlines()[::slope[1]]
        for (i, l) in enumerate(lines):
            if l[slope[0]*i%len(l)] == tree_char:
                cpt += 1
    return cpt

def part_2(grid_file, tree_char, slopes=[]):
    out = math.prod([part_1(grid_file, tree_char, s) for s in slopes])
    return out

def main():
    print(part_1("input.txt", '#', (3,1)))
    print(part_2("input.txt","#",[(1,1),(3,1),(5,1),(7,1),(1,2)]))

if __name__=="__main__":
    main()


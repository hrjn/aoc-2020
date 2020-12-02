
def part_1(input_file=None):
    cpt = 0
    with open(input_file, 'r') as f:
        for line in f:
            ls = line.split(':')
            bounds = [int(x) for x in ls[0][:-2].split('-')]
            if bounds[0] <= ls[-1].count(ls[0][-1]) <= bounds[1]:
                cpt += 1
    return cpt

def part_2(input_file=None):
    cpt = 0
    with open(input_file, 'r') as f:
        for line in f:
            ls = line.split(':')
            bounds = [int(x)-1 for x in ls[0][:-2].split('-')]
            letter = ls[0][-1]
            pwd = ls[-1][1:]
            if((pwd[bounds[0]] == letter)^(pwd[bounds[1]] == letter)):
                cpt += 1
    return cpt 

def main():
    print(part_1("input.txt"))
    print(part_2("input.txt"))

if __name__ == "__main__":
    main()

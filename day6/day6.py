from collections import Counter

def run(input_file):
    cpt = {"part_1": 0, "part_2": 0}
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')
        cnt = Counter()
        cpt_group = 0
        for l in lines:
            if len(l) == 0:
                cpt["part_1"] += len(list(cnt))
                cpt["part_2"] += len([x[0] for x in cnt.items() if x[1] == cpt_group])
                cnt.clear()
                cpt_group = 0
            else:
                cpt_group += 1
                cnt.update(l)
    return cpt
                
def main():
    print(run("input.txt"))

if __name__ == "__main__":
    main()

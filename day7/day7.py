from collections import Counter

def parse_line(line):
    color, content_raw = tuple(line.split(" bags contain "))
    if content_raw == "no other bags.":
        content = {}
    elif ',' in content_raw:
        content = {" ".join(b.split(" ")[1:-1]).strip(): int(b.split(' ')[0]) for b in content_raw.split(", ")}
    else:
        content = {" ".join(content_raw.split(" ")[1:-1]): content_raw.split(" ")[0]}
    return {"color": color, "contains": content}

def create_rules_dict(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')
    rules_dict = {}
    for l in lines:
        if len(l) > 0:
            rule = parse_line(l)
            rules_dict[rule["color"]] = rule["contains"]
    return rules_dict

def part_1(input_file, target_color="shiny gold"):
    rules = create_rules_dict(input_file)
    bags = [target_color]
    for b in bags:
        cb = [k for k, v in rules.items() if b in v.keys()]
        bags += cb
    return len(set(bags[1:]))

def get_terminal_rules(rules):
    return [k for k,v in rules.items() if not v]

def part_2(input_file, target_color="shiny gold"):
    rules = create_rules_dict(input_file)
    bags = [target_color]
    cpt = 0
    terminal_rules = get_terminal_rules(rules)
    while not(set(bags).issubset(set(terminal_rules))):
        for b in bags:
            cnt = Counter(bags)[b]
            cpt += cnt
            bags = [x for x in bags if x != b]
            r = rules[b]
            for j in range(cnt):
                for k, v in r.items():
                    for i in range(int(v)):
                        bags.append(k)
    return cpt-1

def main():
    input_file = "input.txt"
    target_color="shiny gold"
    print(part_1(input_file, target_color))
    print(part_2(input_file, target_color))

if __name__ == "__main__":
    main()

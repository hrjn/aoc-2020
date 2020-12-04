import re

DEFAULT_FIELDS =  ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
OPT_FIELDS = ["cid"]
HGT_RULES = {"cm": [150,193], "in": [59,76]}

def generate_passport(data):
    passport = {}
    for field in data.rstrip('\n').replace('\n', ' ').split(' '):
        kv = field.split(':')
        passport[kv[0]] = kv[1]
    return passport

def check_hgt(passport, rules):
    for x in [(u, passport["hgt"].split(u)) for u in list(rules.keys())]:
        if len(x[1]) > 1:
            return rules[x[0]][0] <= int(x[1][0]) <= rules[x[0]][1]

def strict_check(passport):
    return all([1920<=int(passport["byr"])<=2002,
                          2010<=int(passport["iyr"])<=2020,
                          2020<=int(passport["eyr"])<=2030,
                          check_hgt(passport, rules=HGT_RULES),
                          re.match(r"^#[0-9a-f]{6}$", passport["hcl"]),
                          passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
                          re.match(r"^[0-9]{9}$", passport["pid"])])

def check_passport(passport, fields, opt_fields):
    pspt_fields = list(passport.keys())
    diff = list(set(pspt_fields)^set(fields))
    if not diff or not set(diff)^set(opt_fields):
        return True
    else:
        return False

def part_1(input_file):
    valid_part_1 = []
    with open(input_file, 'r') as f:
        lines = f.read()
    blocks = lines.split('\n\n')
    for b in blocks:
        passport = generate_passport(b)
        if check_passport(passport, fields=DEFAULT_FIELDS, opt_fields=OPT_FIELDS):
            valid_part_1.append(passport)
    return valid_part_1

def part_2(valid_part_1):
    cpt = 0
    for passport in valid_part_1:
        if strict_check(passport):
            cpt += 1
    return cpt

def main():
    out_part_1 = part_1("input.txt")
    print(len(out_part_1))
    print(part_2(out_part_1))

if __name__ == "__main__":
    main()

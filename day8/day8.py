import time

class BootCode(object):

    def __init__(self):
        self.pos = -1
        self.exe = ("nop", 0)
        self.acc = 0
        self.nxt = 0
        self.bkp = {}
        self.code = []
        self.path = []
        self.exit = 0
    
    def __str__(self):
        return str({k: v for (k, v) in self.__dict__.items() if k != "code"})

    def load(self, input_file=None):
        with open(input_file, 'r') as f:
            lines = [l.strip() for l in f.readlines()]
        lsp = lambda x: x.split(" ")
        self.code = [(lsp(l)[0], int(lsp(l)[1])) for l in lines]
        return self
    
    def save(self):
        self.bkp = {k: v for (k, v) in self.__dict__.items() if k not in ["code", "bkp"]}
        return self
    
    def restore(self, debug=False):
        if debug:
            print("Did not work!" + "\n" + f"Rolling back to state {self.bkp}")
        for (k, v) in self.bkp.items():
            setattr(self, k, v)
        self.bkp = {}
        return self

    
    def step(self, alter=None, debug=False):
        if self.nxt == len(self.code):
           self.exit = 1
           return self
        if not alter:
            self.pos = self.nxt
        self.path.append(self.pos)
        if alter:
            self.save()
            self.exe = alter(self.code[self.pos])
        else:
            self.exe = self.code[self.pos]
        self.acc += (self.exe[1] if self.exe[0] == "acc" else 0)
        self.nxt = self.pos + (self.exe[1] if self.exe[0] == "jmp" else 1)
        if debug:
            print(f"nxt={self.nxt}")
            print(f"limit={len(self.code)}")
            print(self)
            if alter:
                print("(!) Branching")
            print("-------------------------")
            time.sleep(1)
        return self

def part_1(input_file="input.txt"):
    bc = BootCode().load(input_file)
    while bc.nxt not in set(bc.path):
        bc.step()
    return bc.acc

def corrupt(ins):
    mapping = {"jmp": "nop", "nop": "jmp"}
    return ins if ins[0] not in list(mapping.keys()) else (mapping[ins[0]], ins[1])

def part_2(input_file="input.txt", debug=False):
    bc = BootCode().load(input_file)
    while bc.exit == 0:
        bc.step(debug=debug)
        if bc.exe[0] in ["jmp", "nop"]:
            bc.step(alter=corrupt, debug=debug)
            while bc.nxt not in set(bc.path) and bc.exit == 0:
                bc.step(debug=debug)
            else:
                if bc.nxt == len(bc.code):
                    return bc.acc
                else:
                    bc.restore(debug=debug)

def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()

DEFAULTS = {
    "row":{
         "size": 128,
         "steps":{
             "up": "B",
             "down": "F"
             }
         },
    "col":{
        "size": 8,
        "steps":{
            "up": "R",
            "down": "L"
            }
        }
    }

def binpart(seq, ctx, dim, debug=False):
    size = ctx[dim]["size"]
    steps = ctx[dim]["steps"]
    cnt = 1
    pt = [0,size-1]
    for s in list(seq):
        incr = round((size-1)/2**cnt)
        if s == steps["down"]:
            direction = "lower"
            pt = [pt[0],pt[1]-incr]
        elif s == steps["up"]:
            direction = "upper"
            pt = [pt[0]+incr,pt[1]]
        else:
            raise ValueError(f"Invalid sequence character: {s} in {seq}")
        if debug:
            print(f"{s} means to take the {direction} half, keeping rows {pt[0]} through {pt[1]}.")
        cnt += 1
    if debug:
        print(f"You are looking for {dim} {pt[0]}")
    return pt[0]

def get_seat_id(full_seq, ctx, debug=False):
    row_seq = full_seq[:7]
    row = binpart(seq=row_seq, ctx=ctx, dim="row", debug=False)
    col_seq = full_seq[7:]
    col = binpart(seq=col_seq, ctx=ctx, dim="col", debug=False)
    seat_id = int(row) * 8 + int(col)
    if debug:
        print(f"{full_seq}: row {row}, col {col}, seat ID {seat_id}.")
    return seat_id

def part_1(input_file, ctx):
    seat_ids = []
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')
        for l in lines:
            seat_ids.append(get_seat_id(l.strip(), ctx))
    return sorted(seat_ids)

def part_2(input_file, ctx):
    nn = part_1(input_file, ctx)
    for i in range(1,len(nn)-1):
        if nn[i+1]-nn[i] != 1:
            my_seat_id = nn[i] + 1
    return my_seat_id


def main():
    print(part_1("input.txt", DEFAULTS)[-1])
    print(part_2("input.txt", DEFAULTS))

if __name__ == "__main__":
    main()

from itertools import product

occupied_column = [False]*8
occupied_row    = [False]*8
occupied_up     = [False]*15
occupied_down   = [False]*15

# column  raw     up      down
# 012..7  000..0  012..7  765..0
# 012..7  111..1  123..8  876..1
# ......  ......  ......  ......
# 012..7  777..7  789..E  EDC..7

def is_occupied(col, row):
    return (occupied_column[col] or
            occupied_row[row] or
            occupied_up[col+row] or
            occupied_down[7-col+row])

def set_occupied(col, row, b):
    occupied_column[col]     = b
    occupied_row[row]        = b
    occupied_up[col+row]     = b
    occupied_down[7-col+row] = b

exist_answer = True
pieces = []
for row in range(8):
    for col, piece in enumerate(input()):
        if piece=='Q':
            exist_answer = exist_answer and not is_occupied(col, row)
            set_occupied(col, row, True)
            pieces.append((col, row))
            

if not exist_answer:
    print('No Answer')
    exit()

place = [(col, row) for col, row in product(range(8), repeat=2) if not is_occupied(col, row)]

def dfs(n, i_bgn):
    if n==0: return []
    for i in range(i_bgn, len(place)):
        col, row = place[i]
        if is_occupied(col, row): continue
        set_occupied(col, row, True)
        ret = dfs(n-1, i+1)
        if ret != None: return [(col, row)] + ret
        set_occupied(col, row, False)
    return None

ret = dfs(5, 0)
if ret == None:
    print('No Answer')
    exit()

pieces += ret
for row in range(8):
    for col in range(8):
        print('Q' if (col, row) in pieces else '.', end='')
    print()

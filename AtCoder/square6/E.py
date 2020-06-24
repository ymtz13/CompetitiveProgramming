H, W = [int(c) for c in input().split()]

coin = []
ncoin_row = [0]*H
ncoin_col = [0]*W

occupied = [[] for _ in range(W)]
connection_row = [[] for _ in range(H)]

for row in range(H):
    for col, cell in enumerate(input()):
        if cell=='o':
            coin.append((row,col))
            ncoin_row[row]+=1
            ncoin_col[col]+=1
            for r in occupied[col]:
                if r not in connection_row[row]:
                    connection_row[row].append(r)
                if row not in connection_row[r]:
                    connection_row[r].append(row)
            occupied[col].append(row)

row_reachable = [coin[0][0]]
for r_i in row_reachable:
    row_reachable += [r_j for r_j in connection_row[r_i] if r_j not in row_reachable]
        
is_all_connected = True
for irow in range(H):
    if ncoin_row[irow]>0 and irow not in row_reachable:
        is_all_connected = False

odd_row = odd_col = 0
for nc in ncoin_row:
    if nc%2==1:
        odd_row+=1

for nc in ncoin_col:
    if nc%2==1:
        odd_col+=1

if len(coin)==1 or (is_all_connected and odd_row + odd_col <=2):
    print('Possible')
else:
    print('Impossible')

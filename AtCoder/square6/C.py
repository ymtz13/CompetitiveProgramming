H, W = [int(c) for c in input().split()]
B = [input() for h in range(H)]

exist_path=False
row_reachable=[0]
for row_bgn in range(H):
    if B[row_bgn][0]=='#':
        continue
    
    row = [row_bgn]
    for r in range(row_bgn+1, H):
        if B[r][0]=='#':
            break
        row.append(r)   

    for col in range(1,W):
        row_newcol = []
        for r in row:
            if B[r][col]=='.':
                row_newcol.append(r)

        for r in row_newcol:
            for r_ in range(r+1, H):
                if r_ in row_newcol or B[r_][col]=='#':
                    break
                row_newcol.append(r_)

        row = row_newcol

    exist_path = exist_path or row_bgn in row
    if row_bgn in row_reachable:
        row_reachable += [r for r in row if r not in row_reachable]
                
if exist_path and H-1 in row_reachable:
    print('Yay!')
else:
    print(':(')

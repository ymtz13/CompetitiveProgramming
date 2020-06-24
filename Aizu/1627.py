def f(i_match):
    if i_match == n_match: return 1

    key = (tuple(nw), tuple(nl), tuple(match_list[i_match:]))
    if key in memo:
        return memo[key]
    
    i, j = match_list[i_match]

    n = 0
    if nw[i]<k and nl[j]<k:
        nw[i] += 1
        nl[j] += 1
        n += f(i_match+1)
        nw[i] -= 1
        nl[j] -= 1

    if nw[j]<k and nl[i]<k:
        nw[j] += 1
        nl[i] += 1
        n += f(i_match+1)
        nw[j] -= 1
        nl[i] -= 1

    memo[key] = n
    return n

while True:
    n = int(input())
    if n==0 : break
    table = [[0]*n for _ in range(n)]
    k=(n-1)//2
    
    m = int(input())
    nw = [0]*n
    nl = [0]*n
    for _ in range(m):
        x, y = [int(c)-1 for c in input().split()]
        table[x][y] =  1
        table[y][x] = -1
        nw[x] += 1
        nl[y] += 1

    if max(nw)>k or max(nl)>k:
        print(0)
        continue

    match_list = [(i,j) for i in range(n) for j in range(i+1, n) if table[i][j]==0]
    n_match = len(match_list)

    memo = {}
    
    print(f(0))

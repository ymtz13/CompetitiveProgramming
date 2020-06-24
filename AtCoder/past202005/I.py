N = int(input())
R = list(range(N))
C = list(range(N))
RC = [R, C]

Q = int(input())
transpose = False
for _ in range(Q):
    query = tuple(map(int, input().split()))
    t = query[0]
    if t!=3: t, A, B = query

    #print()
    #print(query)
    #print('R:', R)
    #print('C:', C)
    
    if t==1:
        buf = RC[0][A-1]
        RC[0][A-1] = RC[0][B-1]
        RC[0][B-1] = buf

    if t==2:
        buf = RC[1][A-1]
        RC[1][A-1] = RC[1][B-1]
        RC[1][B-1] = buf

    if t==3:
        transpose = not transpose
        RC = RC[::-1]

    if t==4:
        if transpose:
            print(N*RC[1][B-1]+RC[0][A-1])
        else:
            print(RC[1][B-1]+N*RC[0][A-1])

A = [list(map(int, input().split())) for _ in range(9)]

def no():
    print('No')
    exit()

S = set(range(1,10))

for row in A:
    if set(row) !=S:
        no()

for col in zip(*A):
    if set(col) != S:
        no()

for i in (0,3,6):
    for j in (0,3,6):
        s = set()
        for k in range(3):
            for l in range(3):
                s.add(A[i+k][j+l])
        if s!=S:
            no()




print('Yes')
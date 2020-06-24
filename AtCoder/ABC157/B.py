A = [list(map(int, input().split())) for _ in range(3) ]
X = [[0]*3 for _ in range(3)]
N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j]==b: X[i][j]=1

def bingo():
    print('Yes')
    exit()

for i in range(3):
    s = 0
    for j in range(3): s += X[i][j]
    if s==3:
        bingo()
        
for j in range(3):
    s = 0
    for i in range(3): s += X[i][j]
    if s==3:
        bingo()

if X[0][0]+X[1][1]+X[2][2]==3: bingo()
if X[0][2]+X[1][1]+X[2][0]==3: bingo()

print('No')

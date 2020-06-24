import sys
input = sys.stdin.readline

N, Z, W = list(map(int, input().split()))
A = [W] + list(map(int, input().split()))

S = set(A)
GX = [None]*(N-1) + [abs(A[N-1]-A[N])]
GY = [None]*(N-1) + [abs(A[N-1]-A[N])]

GX = [None]*N # GX[i] := YがA[i] を取った直後の状況から到達しうるXにとって最善のスコア
GY = [None]*N # GY[i] := XがA[i] を取った直後の状況から到達しうるYにとって最善のスコア
minGX = 10**20
maxGY = 0

for k in range(N-1, -1, -1):
    GX[k] = max(abs(A[k]-A[N]), maxGY)
    GY[k] = min(abs(A[k]-A[N]), minGX)
    minGX = min(minGX, GX[k])
    maxGY = max(maxGY, GY[k])

print(GX[0])

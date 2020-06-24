N = int(input())
A = list(map(int, input().split()))
X = [0]*(100001)
S = 0
for a in A:
    X[a] += 1
    S += a

Q = int(input())
for _ in range(Q):
    B, C = map(int, input().split())
    nB = X[B]
    X[B] = 0
    X[C] += nB
    S += (C-B)*nB
    print(S)

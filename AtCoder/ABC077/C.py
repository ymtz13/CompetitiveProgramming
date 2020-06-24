N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

nA = nC = 0
ans = 0
for i, b in enumerate(B):
    while nA<N and A[nA]< b: nA += 1
    while nC<N and C[nC]<=b: nC += 1
    ans += nA*(N-nC)

print(ans)

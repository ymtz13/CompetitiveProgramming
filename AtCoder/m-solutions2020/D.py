N = int(input())
A = list(map(int, input().split())) + [-1]
m = 1000
s = 0
for i in range(N):
    if A[i+1]>A[i]:
        n = m//A[i]
        s += n
        m %= A[i]

    if A[i+1]<A[i]:
        m += s*A[i]
        s = 0

print(m)

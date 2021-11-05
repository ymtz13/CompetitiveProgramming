N = int(input())
A = list(map(int, input().split()))
S = sum(A)
_, ans = sorted([(abs(a * N - S), i) for i, a in enumerate(A)])[0]
print(ans)

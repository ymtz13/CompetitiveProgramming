N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for a in A:
  S.append(S[-1] + a)

v = 0
for i, a in enumerate(A[:M], 1):
  v += i * a

ans = v
for i in range(M, N):
  v += A[i]*M
  v -= S[i] - S[i - M]
  ans = max(ans, v)

print(ans)

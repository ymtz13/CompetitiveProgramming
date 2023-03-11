N = int(input())
S = input()
W = list(map(int, input().split()))

C0 = S.count('0')
C1 = S.count('1')

X = sorted([(w, s) for w, s in zip(W, S)])

c0 = c1 = 0
ans = max(C0, C1)
for i, (w, s) in enumerate(X):
  if s == '0': c0 += 1
  if s == '1': c1 += 1

  if i < N - 1 and w == X[i + 1][0]: continue

  ans = max(ans, c0 + C1 - c1)

print(ans)

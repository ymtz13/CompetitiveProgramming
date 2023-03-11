N = int(input())
P = list(map(int, input().split())) + [-1]

ans = []
for i in range(2 * N - 1):
  if (i % 2 == 0 and P[i] > P[i + 1]):
    t = i if P[i] > P[i + 2] else i + 1
    P[t], P[t + 1] = P[t + 1], P[t]
    ans.append(t + 1)

  if i % 2 == 1 and P[i] < P[i + 1]:
    t = i if P[i] < P[i + 2] else i + 1
    P[t], P[t + 1] = P[t + 1], P[t]
    ans.append(t + 1)

print(len(ans))
if ans: print(' '.join(map(str, ans)))

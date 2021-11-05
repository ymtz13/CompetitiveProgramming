from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))

INF = 1 << 60

used = [False] * (N + 1)
for a in A:
  used[a] = True

B = deque([i for i, u in enumerate(used[1:], 1) if not u])

A.append(INF)
B.append(INF)

ans = []
cnt = 0
for i in range(N):
  #print(i, ans, cnt)
  if cnt > 0 and B[0] < A[0] and B[0] < ans[-1]:
    ans.append(B.popleft())
    cnt -= 1
  else:
    ans.append(A.popleft())
    if len(A) == 1: break
    cnt += 1

last = ans[-1]
ans = ans[:-1] + sorted(list(B) + [last], reverse=True)[1:]

print(' '.join(map(str, ans)))

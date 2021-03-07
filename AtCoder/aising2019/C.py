from collections import deque

H, W = map(int, input().split())
M = [[2] * (W+2)]
for _ in range(H):
  M.append([2] + list(map(lambda c: 0 if c=='.' else 1, input())) + [2])
M.append([2]*(W+2))

V = [[False]*(W+2) for _ in range(H+2)]
ans = 0
for sh in range(1, H+1):
  for sw in range(1, W+1):
    if V[sh][sw]: continue
    n = [0, 0]
    queue = deque([(sh, sw)])
    while queue:
      qh, qw = queue.popleft()
      if V[qh][qw]: continue
      V[qh][qw] = True
      c = M[qh][qw]
      n[c] += 1

      for dh, dw in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
        h = qh + dh
        w = qw + dw
        if M[h][w] == 1-c: queue.append((h, w))
    
    ans += n[0]*n[1]

print(ans)

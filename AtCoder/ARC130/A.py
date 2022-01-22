N = int(input())
S = input()

C = []
p = None
cnt = 0
for c in S:
  if c != p and p:
    C.append(cnt)
    cnt = 0
  cnt += 1
  p = c

C.append(cnt)

ans = 0
for cnt in C:
  ans += (cnt - 1) * cnt // 2
print(ans)

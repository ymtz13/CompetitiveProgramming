from collections import deque

N = int(input())
S = input()
T = input()

for s, t in zip(S, T):
    if t == "A":
        break
    if s == "A":
        print(-1)
        exit()

for s, t in zip(S[::-1], T[::-1]):
    if t == "B":
        break
    if s == "B":
        print(-1)
        exit()

cnt = 0
ans = 0
for s, t in zip(S, T):
    if s == "B" and t == "A":
        cnt += 1
        ans += 1
    if s == "A" and t == "B":
        if cnt:
            cnt -= 1
        else:
            ans += 1

print(ans)

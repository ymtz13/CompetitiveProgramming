mod = 998244353

N = int(input())
S = list(map(int, input()))

for x, y in zip(S, S[1:]):
    if x > 1 and y > 1:
        print(-1)
        exit()

if S[0] == 1:
    S = [99] + S

chunks = []
for d in S:
    if d > 1:
        chunk = [d, 0]
        chunks.append(chunk)
    else:
        chunk[1] += 1


cnt = 0
t = 0
for d, n in reversed(chunks):
    cnt += n + 1
    p = (cnt + t) % mod
    t += p * (d - 1)
    t %= mod

ans = p - 1
if S[0] == 99:
    ans -= 1

print(ans % mod)

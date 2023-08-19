S = list(map(int, input()))
C = [0] * 1024
C[0] = 1

ans = 0
f = 0
for v in S:
    f ^= 1 << v
    ans += C[f]
    C[f] += 1

print(ans)

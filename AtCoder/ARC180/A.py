mod = 10**9 + 7

N = int(input())
S = input()
T = [[]]

p = None
for c in S:
    if c == p:
        T.append([])
    T[-1].append(c)
    p = c

ans = 1
for t in T:
    n = 1 + (len(t) - 1) // 2
    ans *= n
    ans %= mod

print(ans)

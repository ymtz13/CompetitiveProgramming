N, K = map(int, input().split())
C = [int(input()) for _ in range(K)]
C.sort()

f = C[0] == 0
if f:
    C = C[1:]

S = [[-1]]
for c in C:
    if S[-1][-1] + 1 != c:
        S.append([])

    S[-1].append(c)

S = S[1:]

if f:
    ans = max(map(len, S)) + 1
    for s0, s1 in zip(S, S[1:]):
        if s0[-1] + 2 == s1[0]:
            ans = max(ans, len(s0) + len(s1) + 1)

else:
    ans = max(map(len, S))

print(ans)

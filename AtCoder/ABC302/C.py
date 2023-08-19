from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

P = list(permutations(range(N), N))

for p in P:
    ok = True
    for i, j in zip(p, p[1:]):
        cnt = 0
        for c1, c2 in zip(S[i], S[j]):
            if c1 != c2:
                cnt += 1
        if cnt != 1:
            ok = False

    if ok:
        print("Yes")
        exit()

print("No")

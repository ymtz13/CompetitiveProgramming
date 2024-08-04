N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**9

t = (0, 0, 0, INF, INF)
T = []

for LE, RE in reversed(P):
    basep, LEp, LMp, RMp, REp = t

    if RE <= LMp:
        base = basep + LMp - RE
        LM = RM = RE

    elif RMp <= LE:
        base = basep + LE - RMp
        LM = RM = LE

    else:
        base = basep
        LM = max(LE, LMp)
        RM = min(RE, RMp)

    t = (base, LE, LM, RM, RE)
    T.append(t)

T.reverse()
a = T[0][2]
ans = [a]

for _, LE, LM, RM, RE in T[1:]:
    if a <= LE:
        anxt = LE
    elif a <= RM:
        anxt = a
    else:
        anxt = RM

    a = anxt
    ans.append(a)

print(*ans)

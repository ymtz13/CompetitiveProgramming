N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N)]

C = [0] * (N + 1)
Actions = [None] * N

for i, (t, x) in reversed(list(enumerate(E))):
    if t == 1:
        if C[x] > 0:
            C[x] -= 1
            Actions[i] = 1
        else:
            Actions[i] = 0
    else:
        C[x] += 1
        Actions[i] = -1

if max(C) > 0:
    print(-1)
    exit()

k = 0
kmax = 0
for a in Actions:
    k += a
    kmax = max(kmax, k)

print(kmax)
print(*[v for v in Actions if v >= 0])

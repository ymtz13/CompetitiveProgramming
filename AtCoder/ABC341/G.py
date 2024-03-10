N = int(input())
A = list(map(int, input().split()))

T = [(a, 1) for a in A]
ans = []

for i in range(N - 1, -1, -1):
    while True:
        t0, l0 = T[i]
        if i + l0 == N:
            break
        t1, l1 = T[i + l0]

        if t0 * l1 < t1 * l0:
            T[i] = (t0 + t1, l0 + l1)
        else:
            break

    ans.append(t0 / l0)

for a in ans[::-1]:
    print(a)

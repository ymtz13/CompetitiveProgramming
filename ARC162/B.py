N = int(input())
P = list(map(int, input().split()))
ans = []


def apply(i, j):
    Q = P[0 : i - 1] + P[i + 1 :]
    return Q[:j] + [P[i - 1], P[i]] + Q[j:]


for k in range(1, N - 1):
    i = P.index(k)

    if i == N - 1:
        ans.append((N - 1, N - 3))
        P = apply(N - 1, N - 3)
        # print(P)
        i = P.index(k)

    if i == k - 1:
        continue

    ans.append((i + 1, k - 1))
    P = apply(i + 1, k - 1)
    # print(P)

if P != sorted(P):
    print("No")
    exit()

print("Yes")
print(len(ans))
for a in ans:
    print(*a)

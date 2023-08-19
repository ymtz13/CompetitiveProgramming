from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
B = sorted(A)

E = [[0] * 4 for _ in range(4)]
for a, b in zip(A, B):
    if a != b:
        E[b - 1][a - 1] += 1

C = [0] * 5

for i, j in permutations(range(4), 2):
    cnt = min(E[i][j], E[j][i])
    E[i][j] -= cnt
    E[j][i] -= cnt
    C[2] += cnt

for i, j, k in permutations(range(4), 3):
    cnt = min(E[i][j], E[j][k], E[k][i])
    E[i][j] -= cnt
    E[j][k] -= cnt
    E[k][i] -= cnt
    C[3] += cnt

for i, j, k, l in permutations(range(4), 4):
    cnt = min(E[i][j], E[j][k], E[k][l], E[l][i])
    E[i][j] -= cnt
    E[j][k] -= cnt
    E[k][l] -= cnt
    E[l][i] -= cnt
    C[4] += cnt

# print(C)

print(C[2] + C[3] * 2 + C[4] * 3)

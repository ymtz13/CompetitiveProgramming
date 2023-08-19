from itertools import permutations, combinations_with_replacement

N, T, M = map(int, input().split())
E = [[0] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    E[A - 1][B - 1] = E[B - 1][A - 1] = 1

Z = 0
for perm in permutations(range(N)):
    for comb in combinations_with_replacement(range(T), N - T):
        cnt = [1] * T
        for c in comb:
            cnt[c] += 1

        i = 0
        for t in range(T):
            team = []
            for c in range(cnt[t]):
                team.append(perm[i])
                i += 1
            # print(team, end="")

        # print()

        Z += 1

print(Z)

S = [input() for _ in range(3)]
T = list(map(int, input()))
ans = [S[t - 1] for t in T]
print(''.join(ans))

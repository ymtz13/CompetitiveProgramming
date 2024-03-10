N = int(input())
S = [input() for _ in range(N)]

for i, si in enumerate(S):
    for j, sj in enumerate(S):
        ss = sj + si
        x = []  # z_algo(ss)


V = [1 << 60] * (N << N)

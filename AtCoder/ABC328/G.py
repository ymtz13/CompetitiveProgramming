INF = 1 << 60

N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Pow2N = 1 << N
M = N * Pow2N
dp = [INF] * M

N, D = map(int, input().split())
if N * D > N * (N - 1) // 2:
    print("No")
    exit()

print("Yes")
for f in range(N):
    for d in range(1, D + 1):
        t = (f + d) % N
        print(f + 1, t + 1)

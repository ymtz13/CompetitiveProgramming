N, K = map(int, input().split())
T = [int(input()) for _ in range(N)]

for i in range(2, N):
  if sum(T[i-2:i+1])<K:
    print(i+1)
    exit()

print(-1)
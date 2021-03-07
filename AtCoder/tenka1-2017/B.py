N = int(input())
AB = sorted([tuple(map(int, input().split())) for _ in range(N)])
print(sum(AB[-1]))
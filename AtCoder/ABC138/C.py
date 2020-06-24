N = int(input())
v = sorted(list(map(int, input().split())))

for _ in range(N-1):
    v = sorted([(v[0]+v[1])/2] + v[2:])

print(v[0])

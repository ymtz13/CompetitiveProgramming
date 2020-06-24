N = int(input())
d = sorted([int(c) for c in input().split()])
print(d[N//2]-d[N//2-1])

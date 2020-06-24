N = int(input())
A = list(map(int, input().split()))
p, q = sorted(A)[N//2-1: N//2+1]
for a in A:
    print(p if a>=q else q)

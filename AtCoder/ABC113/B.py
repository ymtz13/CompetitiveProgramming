N = int(input())
T, A = list(map(int, input().split()))
V = [abs(T-int(h)*0.006-A) for h in input().split()]
m = min(V)
for i,v in enumerate(V):
    if v==m:
        print(i+1)
        break

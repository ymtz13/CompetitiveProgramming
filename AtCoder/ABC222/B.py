N, P = map(int, input().split())
A = list(map(int, input().split()))
ans = len([a for a in A if a < P])
print(ans)

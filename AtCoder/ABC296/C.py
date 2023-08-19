N, X = map(int, input().split())
A = list(map(int, input().split()))
S = set(A)

ans = "No"
for a in A:
    if a + X in S:
        ans = "Yes"

print(ans)

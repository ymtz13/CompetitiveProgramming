N, M = map(int, input().split())
S = input()
T = input()

ans = 3
if S == T[:N]:
    ans -= 2

if S == T[-N:]:
    ans -= 1

print(ans)

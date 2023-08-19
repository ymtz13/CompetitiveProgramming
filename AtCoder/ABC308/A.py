def ans(b):
    print("Yes" if b else "No")
    exit()


S = list(map(int, input().split()))

if S != sorted(S):
    ans(False)
if min(S) < 100 or max(S) > 675:
    ans(False)
if len([v for v in S if v % 25]):
    ans(False)

ans(True)

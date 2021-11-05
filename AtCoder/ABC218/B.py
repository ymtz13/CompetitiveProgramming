from string import ascii_lowercase

P = list(map(int, input().split()))
ans = ''.join([ascii_lowercase[p - 1] for p in P])
print(ans)

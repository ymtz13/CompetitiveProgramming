S, T, X = map(int, input().split())
ans = 'No'
if S < T and S <= X and X < T: ans = 'Yes'
if T < S and (S <= X or X < T): ans = 'Yes'
print(ans)

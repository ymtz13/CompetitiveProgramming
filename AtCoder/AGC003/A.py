S = input()
ans = 'Yes'
if 'N' in S and 'S' not in S: ans = 'No'
if 'S' in S and 'N' not in S: ans = 'No'
if 'E' in S and 'W' not in S: ans = 'No'
if 'W' in S and 'E' not in S: ans = 'No'
print(ans)

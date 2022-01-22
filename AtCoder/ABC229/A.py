S1 = input()
S2 = input()

ans = 'Yes'
if S1 == '#.' and S2 == '.#': ans = 'No'
if S2 == '#.' and S1 == '.#': ans = 'No'
print(ans)

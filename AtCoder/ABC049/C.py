S = [input()]
ans = 'NO'
while S:
    S_new = []
    for s in S:
        if s[:5]=='dream'  : S_new.append(s[5:])
        if s[:7]=='dreamer': S_new.append(s[7:])
        if s[:5]=='erase'  : S_new.append(s[5:])
        if s[:6]=='eraser' : S_new.append(s[6:])
    S = S_new
    if '' in S:
        ans = 'YES'
        break

print(ans)

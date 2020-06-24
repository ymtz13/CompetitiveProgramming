S = input()
sep = [0]
i=0
for i in range(len(S)-1):
    if S[i]=='<' and S[i+1]=='>': sep.append(i+1)
sep.append(i+2)

S += 'X'
ans = 0
center = 0
for i in range(len(sep)-1):
    s = S[sep[i]: sep[i+1]]
    l_max = s.count('>')
    ans += max(center, l_max)
    ans += l_max*(l_max-1)//2

    r_max = s.count('<')
    ans += r_max*(r_max-1)//2
    center = r_max
    
ans += center
print(ans)

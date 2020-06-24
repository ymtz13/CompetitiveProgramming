s = input()
ans = [None]*len(s)
i = 0
for c in s:
    ans[i] = c
    if c=='B': i = max(-1, i-2)
    i += 1
print(*ans[:i], sep='')
    
    
        
    

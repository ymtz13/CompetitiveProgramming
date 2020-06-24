S = input()
t = 0
for i in range(1,len(S)):
    if S[i]!=S[i-1]: t+=1
print(t)

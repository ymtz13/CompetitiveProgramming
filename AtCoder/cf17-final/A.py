S = input()+'_'*10
i = 0
ans = 'YES'
for c in 'AKIHABARA' + '_'*10:
  if S[i]==c: i+=1
  elif c!='A':
    ans = 'NO'
    break

print(ans)
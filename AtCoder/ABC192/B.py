from string import ascii_lowercase, ascii_uppercase
ans = 'Yes'
for i, c in enumerate(input()):
  if i%2==0 and c in ascii_uppercase: ans = 'No'
  if i%2==1 and c in ascii_lowercase: ans = 'No'  
print(ans)

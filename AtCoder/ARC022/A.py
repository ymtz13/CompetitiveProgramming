S = input().upper()
I = C = T = False
for c in S:
  if c=='I': I = True
  if I and c=='C': C = True
  if I and C and c=='T': T = True
print('Yes' if T else 'No')
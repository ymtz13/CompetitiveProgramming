S = input()
AC = S[0]=='A' and S[2:-1].count('C')==1
for c in S[1:]:
    AC *= (c>='a' and c<='z') or c=='C'
print('AC' if AC else 'WA')


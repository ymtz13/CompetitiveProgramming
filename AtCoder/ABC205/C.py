A, B, C = map(int, input().split())

sgnA = '+' if A>=0 or C%2==0 else '-'
sgnB = '+' if B>=0 or C%2==0 else '-'
absDiff = abs(A) - abs(B)

if sgnA == '+' and sgnB == '+': print('>' if absDiff > 0 else '<' if absDiff < 0 else '=')
if sgnA == '+' and sgnB == '-': print('>')
if sgnA == '-' and sgnB == '+': print('<')
if sgnA == '-' and sgnB == '-': print('<' if absDiff > 0 else '>' if absDiff < 0 else '=')

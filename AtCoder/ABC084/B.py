A, B = list(map(int, input().split()))
S = input()
ans = S[A]=='-'
for c in S[:A  ]: ans = ans and (c in '0123456789')
for c in S[A+1:]: ans = ans and (c in '0123456789')
print('Yes' if ans else 'No')

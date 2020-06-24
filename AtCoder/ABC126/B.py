S = input()
a = [int(S[:2]), int(S[2:])]
b = [1<=c and c<=12 for c in a]

if b[0] and b[1]:
    print('AMBIGUOUS')
if b[0] and not b[1]:
    print('MMYY')
if not b[0] and b[1]:
    print('YYMM')
if not b[0] and not b[1]:
    print('NA')

    

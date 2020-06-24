N = int(input())
A = [int(c) for c in input().split()]

A_plus, A_minus = [], []
for a in A:
    if a>0: A_plus.append(a)
    else: A_minus.append(a)

if len(A_minus)%2==0:
    print(sum(A_plus) - sum(A_minus))
elif len(A_plus)==0:
    print(sum(A_plus) - sum(A_minus) + max(A_minus)*2)    
else:
    if min(A_plus) > -max(A_minus):
        print(sum(A_plus) - sum(A_minus) + max(A_minus)*2)
    else:
        print(sum(A_plus) - sum(A_minus) - min(A_plus)*2)
        

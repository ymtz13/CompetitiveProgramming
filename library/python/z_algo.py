S='aaabaaaaabccccc'

A=[None]*len(S)
A[0] = len(S);
i, j = 1, 0
while i < len(S):
    while i+j < len(S) and S[j] == S[i+j]:
        j+=1
    A[i] = j

    print(' i={}'.format(i))
    print(' S[{}:]={}'.format(i,S[i:]))
    print(' A[{}]=j={}'.format(i,j))
    print()
    
    if j == 0:
        i+=1
        continue

    # A[0:j]==A[i:i+j]
    k = 1
    while i+k < len(S) and k+A[k] < j:
        A[i+k] = A[k]
        k+=1
    i += k; j -= k;

print(A)

i=1 # S[i:]=='aabaaab'
A[1]=j=2
1+A[1]==1+2>2

i=2


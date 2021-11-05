N = int(input())
S = input()
S0 = list(S[:N])
S1 = list(S[N:])

Q = int(input())
for i in range(Q):
  T, A, B = map(int, input().split())
  if T==1:
    cA = S0[A-1] if A<=N else S1[A-N-1]
    cB = S0[B-1] if B<=N else S1[B-N-1]

    if A<=N:
      S0[A-1] = cB
    else:
      S1[A-N-1] = cB

    if B<=N:
      S0[B-1] = cA
    else:
      S1[B-N-1] = cA
  
  else:
    S0, S1 = S1, S0
    
print(''.join(S0 + S1))
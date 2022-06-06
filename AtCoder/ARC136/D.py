N = int(input())
A = list(map(int, input().split()))

m = 6
M = 10**m

X = [0] * M
for a in A:
  X[a] += 1

Sprev = X
for k in range(m):
  S = [None] * M
  for c1 in range(0, M, 10**(k + 1)):
    for c2 in range(0, 10**k):
      col = c1 + c2
      S[col] = Sprev[col]
      for d in range(10**k, 10**(k + 1), 10**k):
        S[col + d] = S[col + d - 10**k] + Sprev[col + d]

  Sprev = S

  #print(S)
  #for i in range(0, M, 10):
    #print(S[i:i + 10])

ans = 0
Z = M - 1
for a in A:

  selfcount = True
  for c in str(a):
    if int(c) * 2 >= 10:
      selfcount = False
      break
  if selfcount: 
    ans -= 1
    #print(a)

  #print(a, Z - a, S[Z - a])

  #for b in A:
  #  for cA, cB in zip(str(a)[::-1], str(b)[::-1]):
  #    if int(cA) + int(cB)>=10:
  #      ok = False
  #      break
  #  if ok:
  #    print('---', b)

  ans += S[Z - a]

#print(ans)
print(ans // 2)

#246114 753886 3
#--- 10674       ok
#--- 241644      ok
#--- 732231      ok
#271842 728158 0
#371982 628018 0
#284858 715142 0
#10674 989326 2
#--- 246114      ok
#--- 185123      ok
#532090 467910 0
#--- 36908       ok
#593483 406517 0
#185123 814877 1
#--- 10674       ok
#364245 635755 0
#665161 334839 0
#241644 758356 2
#--- 246114      ok
#--- 732231      ok
#604914 395086 0
#645577 354423 0
#410849 589151 0
#387586 612414 0
#732231 267769 2
#--- 246114      ok
#--- 241644      ok
#952593 47407 0
#249651 750349 0
#36908 963092 1
#--- 532090      ok

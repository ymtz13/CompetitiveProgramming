N = int(input())
Slist = []
Alist = []
for _ in range(N):
    S, A = input().split()
    A = int(A)
    Slist.append(S)
    Alist.append(A)

minA = min(Alist)
for i, a in enumerate(Alist):
    if a == minA:
        j = i
        break

S2 = Slist + Slist
ans = S2[j : j + N]
for a in ans:
    print(a)

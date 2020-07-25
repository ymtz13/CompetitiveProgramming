N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
import heapq

L = [A[0]]
i = 0
ans = 0
for a in A[1:]:
    ans += L[i]
    i += 1
    L.append(a)
    L.append(a)

print(ans)

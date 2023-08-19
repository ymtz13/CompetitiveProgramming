N = int(input())
A = [None] + list(map(int, input().split()))


loop = set()
i = 1
while i not in loop:
    loop.add(i)
    i = A[i]

st = i
i = A[i]
ans = [st]
while i != st:
    ans.append(i)
    i = A[i]

print(len(ans))
print(*ans)

N = int(input())
A = sorted(list(map(int, input().split())))
ai = A[-1]
aj = 0
dist = ai+10
for a in A[:-1]:
    if dist>abs(a-ai/2):
        aj = a
        dist=abs(a-ai/2)

print(ai,aj)

N = int(input())
AB = [[int(c) for c in input().split()] for _ in range(N)]

s=0
possible=True
for a, b in sorted(AB, key=lambda x:x[1]):
    s+=a
    if s>b:
        possible = False
        break

print('Yes' if possible else 'No')

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

C = defaultdict(int)

xor = 0
for a in A:
    xor ^= a
    C[a] += 1

if xor != 0:
    print(-1)
    exit()

OddA = [a for a, c in C.items() if c % 2 == 1]


if OddA and max(OddA) > 1:
    print(max(OddA) - 1)
    exit()

print(0)

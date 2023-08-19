N, L, R = map(int, input().split())
A = list(map(int, input().split()))

T = L + R


def grundy(a):
    return (a % T) // L


s = 0
for a in A:
    s ^= grundy(a)

print("First" if s else "Second")

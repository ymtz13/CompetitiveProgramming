H, W = map(int, input().split())
ans = []
oa = ord("A")

for _ in range(H):
    A = list(map(int, input().split()))
    a = [chr(x - 1 + oa) if x else "." for x in A]
    ans.append(a)

for a in ans:
    print("".join(a))

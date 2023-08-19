T = int(input())

ans = []

for _ in range(T):
    a, s = map(int, input().split())
    t = s - a * 2

    if t < 0:
        ans.append(False)
        continue

    ans.append(not (t & a))


for a in ans:
    print("Yes" if a else "No")

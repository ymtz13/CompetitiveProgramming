N = int(input())
WX = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for h in range(24):
    cnt = 0
    for w, x in WX:
        y = (h + x) % 24
        if 9 <= y < 18:
            cnt += w

    ans = max(ans, cnt)


print(ans)

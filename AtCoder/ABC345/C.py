S = input()
orda = ord("a")
cnt = [0] * 26
for c in S:
    cnt[ord(c) - orda] += 1

s = 0
ans = 0
for c in cnt:
    ans += s * c
    s += c

if max(cnt) > 1:
    ans += 1

print(ans)

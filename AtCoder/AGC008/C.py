I, O, _, J, L, _, _ = map(int, input().split())

ans = O
if I > 0 and J > 0 and L > 0 and (I % 2 + J % 2 + L % 2 >= 2):
  ans += 3
  I -= 1
  J -= 1
  L -= 1

ans += (I // 2) * 2 + (J // 2) * 2 + (L // 2) * 2
print(ans)

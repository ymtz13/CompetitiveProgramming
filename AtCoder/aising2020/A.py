L, R, d = map(int, input().split())
print(len([x for x in range(L, R+1) if x%d==0]))

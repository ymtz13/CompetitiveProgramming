a, b = list(map(int, input().split()))
h = 0
for i in range(1,b-a): h+=i
print(h-a)

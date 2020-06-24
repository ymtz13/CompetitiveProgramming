N = int(input())
A = list(map(int, input().split()))

for a in A:
    print('{:10b}'.format(a))

N = int(input())
A = list(map(int, input().split()))[::2]
print(len([x for x in A if x%2==1]))

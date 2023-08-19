from bisect import bisect

Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

A2 = []
A3

for query in Queries:
    c = query[0]

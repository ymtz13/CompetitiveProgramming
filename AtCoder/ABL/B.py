A, B, C, D = map(int, input().split())
print('Yes' if (C<=A and A<=D or C<=B and B<=D or A<=C and C<=B or A<=D and D<=B) else 'No')

s = input()
ans = s[(len(s)+1)//2:].count('g') - s[:(len(s)+1)//2].count('p')
print(ans)

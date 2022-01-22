S = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
W = int(input())
for i in range(0, 100, W):
  s = S[i:i + W]
  if len(s): print(s)

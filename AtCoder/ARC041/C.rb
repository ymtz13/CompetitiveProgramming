N, L = gets.split.map(&:to_i)
nR = 1
k = [[[],[]]]
N.times do
  x, d = gets.split
  if d=='R' then
    k << [[],[]] if nR==0
    
    nR+=1
    k[-1][0] << x.to_i
  else
    nR = 0
    k[-1][1] << x.to_i
  end
end

ans = 0
k.each do |t|
  sR = sL = 0
  
  nR = t[0].length
  xR = nR>0 ? t[0][-1] : 0
  t[0].each_with_index do |x, idx|
    sR += xR-x-1-(nR-2-idx)
  end

  nL = t[1].length
  xL = nL>0 ? t[1][0] : L+1
  t[1].each_with_index do |x, idx|
    sL += x-xL-1 - (idx-1)
  end
  
  ans += (xL-xR-1)*[nR,nL].max + sR + sL
  
end

puts ans

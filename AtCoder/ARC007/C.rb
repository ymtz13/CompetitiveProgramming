C = gets.chomp
N = C.length
x = 0
C.split('').each_with_index do |c, idx|
  x |= 1<<idx | 1<<(idx+N) if c=='o'
end

ans = N
M = 1<<N
M.times do |f|
  ntv = 0
  z = 0
  N.times do |i|
    if (f>>i&1)==0 then next end
    ntv += 1
    z |= x<<i
  end
  if (z>>N)%M==M-1 then ans=[ans,ntv].min end
end

puts ans

N, L = gets.split.map(&:to_i)
swap = []
L.times do
  gets.split('|').each_with_index do |c, idx|
    swap << idx-1 if c=='-'
  end
end

g = gets.index('o')/2

N.times do |st|
  i = st
  swap.each do |s|
    if i==s then i+=1 elsif i==s+1 then i-=1 end
  end
  puts st+1 if i==g
end

R, C = gets.split.map(&:to_i)
sy, sx = gets.split.map(&:to_i)
gy, gx = gets.split.map(&:to_i)
m = []
R.times { m.push gets.chomp.split('') }

queue = [[sx-1, sy-1, 0]]
iq = 0
while queue.length>iq do
  x, y, d = queue[iq]
  iq+=1
  if m[y][x]!='.' then next end
  
  m[y][x] = d
  queue.push([x+1, y  , d+1])
  queue.push([x-1, y  , d+1])
  queue.push([x  , y+1, d+1])
  queue.push([x  , y-1, d+1])
end

puts m[gy-1][gx-1]

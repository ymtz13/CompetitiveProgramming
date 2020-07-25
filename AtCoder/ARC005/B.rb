x, y, W = gets.split
x = x.to_i-1
y = y.to_i-1
dx = if W.include? 'R' then +1 elsif W.include? 'L' then -1 else 0 end
dy = if W.include? 'D' then +1 elsif W.include? 'U' then -1 else 0 end
c = []
9.times { c << gets.chomp }

ans = []
4.times {
  ans << c[y][x]
  x += dx
  y += dy
  if x<0 then x=1; dx=+1 end
  if x>8 then x=7; dx=-1 end
  if y<0 then y=1; dy=+1 end
  if y>8 then y=7; dy=-1 end
  
}
puts ans.join

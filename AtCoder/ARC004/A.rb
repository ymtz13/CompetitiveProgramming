xy = []
gets.to_i.times { xy << gets.split.map(&:to_i) }

def dist(p1, p2)
  dx = p1[0] - p2[0]
  dy = p1[1] - p2[1]
  return (dx*dx+dy*dy)**0.5
end

ans = 0
xy.each do |p1|
  xy.each do |p2|
    ans = [ans, dist(p1, p2)].max
  end
end

puts ans

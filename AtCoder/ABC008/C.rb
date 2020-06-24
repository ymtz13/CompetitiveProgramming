N = gets.to_i
c = []
N.times { c << gets.to_i }
d = c.map do |x|
  c.filter { |y| x%y==0 }.length-1
end

ans = 0
d.each do |e|
  ans += (e+2)/2/(e+1).to_f
end

puts ans

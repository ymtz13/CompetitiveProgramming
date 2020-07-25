m, n, x = gets.split.map(&:to_i)
ans = x
while x>=m do
  k = n*(x/m)
  ans += k
  x = k + x%m
end
puts ans

c = [1,2,3,4,5,6]
(0..gets.to_i%30-1).each { |i|
  c[i%5], c[i%5+1] = c[i%5+1], c[i%5]
}
puts c.join

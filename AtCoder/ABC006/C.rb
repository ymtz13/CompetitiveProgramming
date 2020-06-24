N, M = gets.split.map(&:to_i)
ans = "-1 -1 -1"
(0..N).each { |x|
  #  y +  z = N-x
  # 3y + 4z = M-2x
  # z = M-2x-3(N-x) = -3N+M+x
  z = -3*N + M + x
  y = N-x-z
  ans = "#{x} #{y} #{z}" if y>=0 && y<=N && z>=0 && z<=N  
}
puts ans

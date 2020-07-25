E = gets.split
B = gets.chomp
L = gets.split
N = E.filter{|e| L.include?(e) }.count
ans = [0, 0, 0, 5, 4, (L.include?(B) ? 2 : 3), 1][N]
puts ans

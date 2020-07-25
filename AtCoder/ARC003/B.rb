N = gets.to_i
s = []
N.times { s << gets.chomp.reverse }
s.sort!
s.each {|x| puts x.reverse }

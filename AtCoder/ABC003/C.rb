N, K = gets.split.map(&:to_i);
A = gets.split.map(&:to_i).sort;
ans=0
A.slice(-K..-1).each{|a| ans=(ans+a)/2.0}
puts ans

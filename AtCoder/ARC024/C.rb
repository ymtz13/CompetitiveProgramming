N, K = gets.split.map(&:to_i)
S = gets.chomp

if K*2>N then
  puts 'NO'
  exit
end

dd = []
('a'..'z').each_with_index do |c, idx|
  s = [0]
  S.each_char {|x| s << (x==c ? s[-1]+1 : s[-1])}

  d = []
  (N-K+1).times do |i|
    d << s[i+K]-s[i]
  end
  dd << d
end

z = {}
(N-K+1).times do |i|
  key = []
  dd.each {|d| key << d[i]}
  z[key] = [] unless z.has_key?(key)
  z[key] << i
end

z.each do |k, v|
  if v[0]+K<=v[-1] then
    puts "YES"
    exit
  end
end

puts "NO"

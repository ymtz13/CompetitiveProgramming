M = [nil]*10
gets.split.map(&:to_i).each_with_index do |b, idx|
  M[b] = idx
end

alist = []

gets.to_i.times do
  a = gets.chomp
  x = 0
  d = 1
  a.reverse.each_char do |c|
    x += M[c.to_i] * d
    d *= 10
  end

  alist << [x, a]
end

alist.sort.each do |x, a|
  puts a
end

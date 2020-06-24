T = gets.to_i
N = gets.to_i
A = gets.split(' ').map(&:to_i)
M = gets.to_i
B = gets.split(' ').map(&:to_i)

i = 0
ok = false
B.each do |b|
  ok = false
  (i..N-1).each do |i|
    a = A[i]
    if b-T<=a && a<=b then ok = true; break; end;
    if a>b then break end
  end
  if !ok then break end
  i+=1
end

puts (if ok then 'yes' else 'no' end)

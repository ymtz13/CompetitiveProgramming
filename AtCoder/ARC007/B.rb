N, M = gets.split.map(&:to_i)
c = [nil] + (1..N).to_a
d = [nil] + (1..N).to_a
x = 0

M.times do
  disk = gets.to_i
  ic = d[disk]
  c[ic] = x
  d[x] = ic
  d[disk] = nil
  x = disk
end

puts c[1..N].join("\n")

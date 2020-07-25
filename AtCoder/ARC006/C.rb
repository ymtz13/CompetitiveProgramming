piles = [[100001]]
gets.to_i.times do
  w = gets.to_i
  m = 999999
  i = nil
  piles.each_with_index do |pile, idx|
    last = pile[-1]
    if last>=w && last<m then
      m = pile[-1]
      i = idx
    end
  end

  if i then
    piles[i] << w
  else
    piles << [w]
  end
end

puts piles.count

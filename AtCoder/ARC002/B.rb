require 'date'
YMD = gets.split('/').map(&:to_i)
d = Date.new(YMD[0], YMD[1], YMD[2])

365.times do
  break if d.year%d.month==0 && (d.year/d.month)%d.day==0
  d += 1
end

puts d.strftime("%Y/%m/%d")

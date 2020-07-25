D = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = 0
dd = []
12.times {|m| dd << (d+=D[m]); }

h = [false]*366
gets.to_i.times do
  m, d = gets.split('/').map(&:to_i)
  h[dd[m-1]+d-1] = true
end

n = 0
streak = 0
ans = 0
366.times do |day|
  if (day+1)%7<=1 then n+=1 end
  if h[day] then n+=1 end

  if n>0 then
    streak+=1
    ans = [ans, streak].max
    n-=1
  else
    streak=0
  end
end

puts ans

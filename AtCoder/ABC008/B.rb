N = gets.to_i
d = {}
N.times {
  s = gets
  if d[s]==nil then d[s]=0 end
  d[s]+=1
}
max = d.values.max
ans = nil
d.each_key {|k| if max==d[k] then ans=k end}
puts ans

a=[0,0,1]
n=gets.to_i
(n-3).times {|i| a[i+3]=(a[i]+a[i+1]+a[i+2])%10007}
puts a[n-1]

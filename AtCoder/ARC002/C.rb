N = gets.to_i
C = gets.chomp
K = 'ABXY'.split('')
KK = K.product(K).map(&:join)

ans = N

KK.each do |l|
  KK.each do |r|
    i = 0
    k = 0
    while i<N do
      k+=1
      if i<N-1 && (C[i,2]==l || C[i,2]==r) then
        i+=2
      else
        i+=1
      end
    end

    ans = [ans, k].min
    
  end
end

puts ans

#        abcdefghijklmnopqrstuvwxyz
table = '_112_498_38579_74063_526_0'
gets;
puts gets.split.map {|w| w.downcase.gsub(/[^a-z]/, '').split('').map{|c| table[c.ord-'a'.ord]}.join.gsub('_', '') }.filter{|w| w.length>0}.join(' ')

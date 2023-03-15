let _ = read_line() in
let s = read_line() in
let j = Seq.fold_left (fun cnt c -> if c = 'J' then cnt + 1 else cnt) 0 (String.to_seq s) in
let o = Seq.fold_left (fun cnt c -> if c = 'O' then cnt + 1 else cnt) 0 (String.to_seq s) in
let i = Seq.fold_left (fun cnt c -> if c = 'I' then cnt + 1 else cnt) 0 (String.to_seq s) in
let ans = String.make j 'J' ^ String.make o 'O' ^ String.make i 'I' in
print_endline ans;

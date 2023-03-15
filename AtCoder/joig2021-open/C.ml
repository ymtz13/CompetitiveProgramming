let n = int_of_string (read_line ());;
let aarr = List.map int_of_string (String.split_on_char ' ' (read_line ()));;
let cnt = List.fold_left (fun cnt x -> cnt + x) 0 aarr;;
let fold (ans, curr) x = let next = curr + 1 - x*2 in ((min ans next), next);;
let ans = List.fold_left fold (cnt, cnt) aarr;;
print_endline (string_of_int (fst ans));;

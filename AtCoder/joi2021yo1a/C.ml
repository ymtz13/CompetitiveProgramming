let read_int_list () = 
  let line = read_line() in 
  List.map int_of_string (String.split_on_char ' ' line);;

read_line();;

let aarr = read_int_list() in
let barr = read_int_list() in
let ans = List.filter (fun a -> List.exists (fun b -> a=b ) barr) aarr in
let ans = List.sort compare ans in
print_endline (String.concat "\n" (List.map string_of_int ans));

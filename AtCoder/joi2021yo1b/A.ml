let read_int_tuple3 () =
  let str = read_line () in
  let list = List.map int_of_string (String.split_on_char ' ' str) in
    match list with
      | e1::e2::e3::[] -> (e1, e2, e3)
      | _ -> (0, 0, 0);;

let ans = 
  let (a, b, c) = read_int_tuple3 () in
  if a<=c && c<b then 1 else 0;;

print_endline (string_of_int ans)

let ans = 
  let len = int_of_string (read_line ()) in
  let str = read_line () in
  let il = String.index_from_opt str 0 'I' in 
  let ir = String.rindex_from_opt str (len -1) 'I' in 
    match (il, ir) with
      | (Some l, Some r) -> String.contains (String.sub str l (r-l+1)) 'O'
      | _ -> false;;

print_endline (if ans then "Yes" else "No");;

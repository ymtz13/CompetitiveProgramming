let abc = read_line() in 
let a::b::c::[] = List.map int_of_string (String.split_on_char ' ' abc) in
let maxv = max a (max b c) in
let minv = min a (min b c) in
let ans = a+b+c - maxv-minv in
print_endline (string_of_int ans);

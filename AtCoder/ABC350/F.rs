use std::collections::VecDeque;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s = read_line().into_bytes();
    let n = s.len();

    let mut stack = VecDeque::new();
    let mut pairs = vec![n + 1; n];

    for i in 0..n {
        if s[i] == b'(' {
            stack.push_back(i);
        }
        if s[i] == b')' {
            let j = stack.pop_back().unwrap();
            pairs[i] = j;
            pairs[j] = i;
        }
    }

    let mut dir: i64 = 1;
    let mut i: i64 = 0;
    let mut ans = vec![];

    while 0 <= i && i < (n as i64) {
        let ii = i as usize;
        let c = s[ii];

        if c == b'(' || c == b')' {
            i = pairs[ii] as i64;
            dir = -dir;
        } else {
            ans.push(if dir == 1 { c } else { c ^ 32 });
        }

        i += dir;
    }

    // println!("{ans:?}");
    println!("{}", String::from_utf8(ans).unwrap());
}

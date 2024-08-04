fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let ss = read_line().into_bytes();
    let n = ss.len();

    let mut l = 0;
    let mut r = n - 1;
    let mut ans = 0;

    let x = b'x';

    while l < r {
        let cl = ss[l];
        let cr = ss[r];

        if cl == cr {
            l += 1;
            r -= 1;
            continue;
        } else if cl == x {
            ans += 1;
            l += 1;
        } else if cr == x {
            ans += 1;
            r -= 1;
        } else {
            ans = -1;
            break;
        }
    }

    println!("{ans}")
}

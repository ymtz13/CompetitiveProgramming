fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let ss = read_line().into_bytes();
    let ss: Vec<usize> = ss.iter().map(|v| (v - b'a') as usize).collect();
    let n = ss.len();

    let mut vv: Vec<u32> = vec![n as u32; 1 << 26];
    vv[0] = 0;
    let mut b = 0;

    for &c in &ss {
        b ^= 1 << c;

        let mut v = vv[b];
        for d in 0..26 {
            let i = b ^ (1 << d);
            v = std::cmp::min(v, vv[i]);
        }

        vv[b] = std::cmp::min(vv[b], v + 1);
    }

    println!("{}", if b > 0 { vv[b] } else { 1 });
}

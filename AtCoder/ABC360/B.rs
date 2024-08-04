fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let st = read_line();
    let st: Vec<_> = st.split_whitespace().collect();
    let s: Vec<_> = st[0].bytes().collect();
    let t: Vec<_> = st[1].bytes().collect();

    for w in 1..s.len() {
        for c in 0..w {
            let mut i = c;
            let mut z = vec![];
            while i < s.len() {
                z.push(s[i]);
                i += w;
            }
            // println!("{w} {c} {z:?}");

            if z == t {
                println!("Yes");
                return;
            }
        }
    }

    println!("No");
}

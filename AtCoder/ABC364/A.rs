fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

type Int = usize;

fn read_vec() -> Vec<Int> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (Int, Int) {
    let v = read_vec();
    (v[0], v[1])
}

fn read_iii() -> (Int, Int, Int) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let n = read_vec()[0];
    let mut ss: Vec<_> = (0..n).map(|_| read_line()).collect();

    for i in 1..n - 1 {
        if ss[i] == "sweet" && ss[i - 1] == "sweet" {
            println!("No");
            return;
        }
    }

    println!("Yes");
}

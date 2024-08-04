fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut aa = vec![0];
    aa.extend(read_vec());

    let mut pos = vec![0; n + 1];
    for (i, a) in aa.iter().enumerate() {
        pos[*a] = i;
    }

    let mut ans = vec![];

    for i in 1..n {
        let j = pos[i];
        if i == j {
            continue;
        }

        let ai = aa[i];

        pos[ai] = j;
        aa[j] = ai;

        ans.push((i, j));
    }

    println!("{}", ans.len());
    for &(i, j) in &ans {
        println!("{i} {j}");
    }
}

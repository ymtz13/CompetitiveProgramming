fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n = read_line().parse().unwrap();
    let mut ans = vec![vec![0; n]; 2];

    for i in 0..n {
        let cc: Vec<_> = read_line().bytes().map(|v| if v == b'#' { 1 } else { 0 }).collect();

        let aa = cc.iter().enumerate().map(|(j, c)| {
            let mut cnt = ans[i][j] + c;
            if j > 0 {
                cnt += ans[i + 1][j - 1];
            }
            if j < n - 1 {
                cnt += ans[i + 1][j + 1];
            }
            cnt % 2
        });

        ans.push(aa.collect());

        // println!("{:?}", cc);
    }

    for aa in &ans[1..=n] {
        let s = String::from_utf8(aa.iter().map(|&v| if v == 1 { b'#' } else { b'.' }).collect()).unwrap();

        println!("{}", s);
    }
}

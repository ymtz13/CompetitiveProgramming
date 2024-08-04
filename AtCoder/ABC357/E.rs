fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut aa = vec![0];
    aa.extend(read_vec());

    let inf = n + 10;

    let mut visited = vec![inf; n + 1];
    let mut ans = vec![inf; n + 1];

    for st in 1..=n {
        if visited[st] != inf {
            continue;
        }

        let mut i = st;
        let mut v = 0;
        let mut ii = vec![];

        while visited[i] == inf {
            ii.push(i);
            visited[i] = v;
            i = aa[i];
        }

        if ans[i] == inf {
            let mut size = 0;
            for &j in ii.iter().rev() {
                size += 1;
                if j == i {
                    break;
                }
            }

            let mut in_loop = true;
            for &j in ii.iter().rev() {
                ans[j] = size;
                if j == i {
                    in_loop = false;
                }
                if !in_loop {
                    size += 1;
                }
            }
        } else {
            let mut size = ans[i];
            for &j in ii.iter().rev() {
                size += 1;
                ans[j] = size;
            }
        }
    }

    let ans: usize = ans[1..].iter().sum();
    println!("{ans}");
}

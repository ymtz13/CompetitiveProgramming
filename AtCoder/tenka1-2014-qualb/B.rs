fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn z_algo<T: std::cmp::PartialEq>(arr: &Vec<T>) -> Vec<usize> {
    let l = arr.len();
    let mut ret = vec![l];
    let mut i = 1;
    let mut jnxt = 0;
    while i < l {
        let mut j = jnxt;
        while i + j < l && arr[j] == arr[i + j] {
            j += 1;
        }

        ret.push(j);

        jnxt = 0;
        for k in 1..=j {
            if k + ret[k] >= j {
                jnxt = j - k;
                break;
            }
            ret.push(ret[k]);
        }

        i = ret.len();
    }

    ret
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let s = read_line().into_bytes();
    let mut tt = vec![];
    for _ in 0..n {
        let mut t = s.clone();
        t.push(b'_');
        t.extend(read_line().into_bytes());

        let z = z_algo(&t);
        let zz: Vec<_> = z[s.len() + 1..].iter().map(|&v| v).collect();

        tt.push(zz);
    }

    println!("{:?}", s);
    println!("{:?}", tt);
}

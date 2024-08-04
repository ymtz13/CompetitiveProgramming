fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn gray(m: usize) -> Vec<usize> {
    let mut ret = vec![0, 0];
    for i in 1..m {
        let mut ret_nxt = vec![];
        for &v in &ret {
            ret_nxt.push(v);
            ret_nxt.push(i);
        }
        ret = ret_nxt;
    }
    ret.pop();
    ret
}

fn main() {
    // let k = 4;
    // let gg = gray(k);
    // println!("{gg:?}");

    // let mut z = 0;
    // let mut ff = vec![false; 1 << k];
    // for &g in &gg {
    //     z ^= 1 << g;
    //     println!("{g} {z:#09b}");
    //     assert!(!ff[z]);
    //     ff[z] = true;
    // }

    let (n, a, b) = read_uuu();

    let c = a ^ b;
    let mut n1 = 0;
    for i in 0..n {
        if (c >> i) & 1 == 1 {
            n1 += 1;
        }
    }
    if n1 % 2 == 0 {
        println!("NO");
        return;
    }
    println!("YES");

    let mut x = 0;
    let mut ops = vec![];
    for i in (0..n).rev() {
        let bit = 1 << i;
        if x & bit == c & bit {
            ops.push(i);
            x ^= bit;
        }
        if i > 0 {
            ops.extend(gray(i));
            x ^= bit >> 1;
        }
        ops.push(i);
        x ^= bit;
    }

    let mut z = 0;
    let mut ans = vec![];
    for &op in &ops {
        ans.push(z ^ a);
        z ^= 1 << op;
    }

    println!("ans.len() = {},  2**N-1 = {}", ans.len(), (1 << n) - 1);

    let mut ff = vec![false; 1 << n];
    for &a in &ans {
        println!("{a:#010b} {}", ff[a]);
        ff[a] = true;
    }
}

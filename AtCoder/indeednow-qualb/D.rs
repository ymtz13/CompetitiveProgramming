use std::io;
use std::convert::TryFrom;

fn main() {
    let mut nc = String::new();
    io::stdin().read_line(&mut nc).unwrap();
    
    let nc: Vec<&str> = nc.split_whitespace().collect();
    let n: usize = nc[0].parse().unwrap();
    let c: usize = nc[1].parse().unwrap();

    let mut a = String::new();
    io::stdin().read_line(&mut a).unwrap();
    let a: Vec<&str> = a.split_whitespace().collect();

    let mut k: Vec<Vec<u32>> = Vec::new();
    for _ in 0..n+1 {
        k.push(Vec::new());
    }

    println!("{:?}", a);

    for (i, &v) in a.iter().enumerate() {
        let v: usize = (*v).parse().unwrap();
        println!("{}", v);
        k[v].push(i.try_into().unwrap());
    }
    k.remove(0);
    println!("{:?}", k);

    let mut ans = 0;
    for mut p in k {
        p.push(n);
        println!("{:?}", p);
        let mut pre: i32 = -1;
        for i in p {
            let l  = i - pre - 1;
            ans += l*(l+1)/2;
            pre = i;
        }
    }
    println!("{}", ans);

}

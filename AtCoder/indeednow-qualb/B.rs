use std::io;

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    let s = s.trim().as_bytes();

    let mut t = String::new();
    io::stdin().read_line(&mut t).unwrap();
    let t = t.trim().as_bytes();

    let n = s.len();

    if s.len() != t.len() {
        println!("-1");
        return ()
    }

    //println!("{:?} {:?} {}", s, t, n);

    for i in 0..n {
        //println!("[{}]", i);
        let mut ok = true;
        for j in 0..n {
            ok = ok & (t[j] == s[(n-i+j)%n]);
            //println!("{} - {}, {}", t[j], s[(n-i+j)%n], ok);
            if !ok {
                break;
            }
        }

        if ok {
            println!("{}", i);
            return ()
        }
    }

    println!("-1");
}

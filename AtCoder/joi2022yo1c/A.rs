use std::str::FromStr;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_tuple3<T: FromStr, U: FromStr, V: FromStr>() -> Result<(T, U, V), ()> {
    let items = input();
    let mut items = items.split_whitespace();

    let t = items.next().unwrap().parse();
    let u = items.next().unwrap().parse();
    let v = items.next().unwrap().parse();

    if let (Ok(t), Ok(u), Ok(v)) = (t, u, v) {
        return Ok((t, u, v));
    }

    Err(())
}

fn read_vec<T: FromStr>() -> Result<Vec<T>, ()> {
    let items = input();
    let mut result: Vec<T> = Vec::new();

    for item in items.split_whitespace() {
        match item.parse() {
            Ok(v) => result.push(v),
            Err(_) => return Err(()),
        }
    }

    Ok(result)
}

fn main() {
    let a: usize = input().trim().parse().unwrap();
    let b: usize = input().trim().parse().unwrap();
    println!("{}", b - a);
}

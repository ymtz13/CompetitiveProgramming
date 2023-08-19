fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

#[derive(Debug)]
struct ParseVecError;

fn parse_vec<T: std::str::FromStr>() -> Result<Vec<T>, ParseVecError> {
    let items = input();
    let items = items.split_whitespace();

    let mut result: Vec<T> = Vec::new();

    for item in items {
        result.push(item.parse().map_err(|_| ParseVecError)?);
    }

    Ok(result)
}

fn main() {
    input();
    let a: Vec<usize> = parse_vec().unwrap();
    let mut b = vec![0; 200];

    for v in &a {
        b[*v] += 1;
    }

    b.sort();
    b.reverse();

    println!("{:?}", b[0]);
}

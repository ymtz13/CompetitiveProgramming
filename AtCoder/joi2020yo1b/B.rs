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
    let nab: Vec<usize> = parse_vec().unwrap();
    let a = nab[1] - 1;
    let b = nab[2];

    let s = input();
    let s = s.trim();

    let chars: Vec<char> = s.chars().collect();

    let mut mid = Vec::from(&chars[a..b]);
    mid.reverse();

    let ans = vec![Vec::from(&chars[..a]), mid, Vec::from(&chars[b..])].concat();

    println!(
        "{}",
        ans.iter()
            .map(|c| c.to_string())
            .collect::<Vec<_>>()
            .join("")
    );
}

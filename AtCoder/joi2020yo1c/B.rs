fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let s = input();
    let s = s.trim();

    let mut ans = vec!['_', '_'];

    for c in s.chars() {
        ans.push(c);

        let c0 = ans[ans.len() - 3];
        let c1 = ans[ans.len() - 2];
        let c2 = ans[ans.len() - 1];

        if c0 == 'j' && c1 == 'o' && c2 == 'i' {
            ans.pop();
            ans.pop();
            ans.pop();
            ans.append(&mut vec!['J', 'O', 'I']);
        }
    }

    println!(
        "{}",
        &(ans
            .iter()
            .map(|c| c.to_string())
            .collect::<Vec<_>>()
            .concat())[2..]
    );
}

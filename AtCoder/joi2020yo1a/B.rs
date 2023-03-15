use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).expect("");
    io::stdin().read_line(&mut input).expect("");
    let input = input.trim().chars();

    // let filter = input.filter(|c| c == &'x');
    let filter = input.filter(|c| "aiueo".contains(*c));
    // let filtered: Vec<_> = filter.collect();
    let count = filter.count();

    // println!("{:#?}", input);
    // println!("{:#?}", filter);
    // println!("{:#?}", filtered);
    println!("{}", count);
}

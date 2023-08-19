fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    input();
    let mut xlist = read_int_vec();
    input();
    let alist = read_int_vec();

    let mut cells = vec![-1; 2100];
    for (i, x) in xlist.iter().enumerate() {
        cells[*x] = i as i32;
    }
    cells[2020] = 0;

    for a in &alist {
        let a = (*a) - 1;
        let pos = xlist[a];
        if cells[pos + 1] != -1 {
            continue;
        }

        cells[pos] = -1;
        cells[pos + 1] = a as i32;
        xlist[a] = (pos + 1) as usize;
    }

    for x in &xlist {
        println!("{}", x);
    }
}

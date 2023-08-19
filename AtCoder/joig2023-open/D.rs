use std::convert::TryInto;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_list() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    let hw = read_int_list();
    let h = hw[0];
    let w = hw[1];
    let w_i64: i64 = w.try_into().unwrap();
    let h_i64: i64 = h.try_into().unwrap();

    let mut board = Vec::<Vec<char>>::new();
    for _ in 0..h {
        let row = input().chars().collect();
        board.push(row);
    }

    let mut count_row = Vec::<i64>::new();
    let mut count_col = Vec::<i64>::new();
    let mut count_tot = 0;

    for _ in 0..h {
        count_row.push(0);
    }
    for _ in 0..w {
        count_col.push(0);
    }

    for r in 0..h {
        for c in 0..w {
            if board[r][c] == '#' {
                count_row[r] += 1;
                count_col[c] += 1;
                count_tot += 1;
            }
        }
    }

    let mut ans = 0;

    for (r, crow) in count_row.iter().enumerate() {
        let mut a = h_i64 * w_i64;

        for (c, ccol) in count_col.iter().enumerate() {
            let cross = if board[r][c] == '#' { 1 } else { 0 };
            let count_other = count_tot - crow - ccol + cross * 2;
            let crow_flip = w_i64 - crow + cross - 1;
            let ccol_flip = h_i64 - ccol + cross - 1;
            let ctot_flip = count_other + crow_flip + ccol_flip;

            // println!("{r}, {c}, {ctot_flip}");

            a = std::cmp::min(a, ctot_flip);
        }

        ans = std::cmp::max(ans, a);
    }

    // println!("{h} {w} {board:#?}");
    // println!("count_row {count_row:#?}");
    // println!("count_col {count_col:#?}");

    println!("{} {}", ans, h_i64 * w_i64 - ans);
}

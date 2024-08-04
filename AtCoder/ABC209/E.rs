static DRAW: usize = 0;
static LOSE: usize = 1;
static WIN: usize = 2;

fn read_line() -> String {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    String::from(inp.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let m: usize = 52 * 52 * 52;

    let mut edges: Vec<Vec<usize>> = (0..m).map(|_| vec![]).collect();
    let mut words = vec![];
    let mut counts = vec![-1; m];
    for _ in 0..n {
        let s: Vec<_> = read_line().bytes().map(|c| if c >= b'a' { c - b'a' + 26 } else { c - b'A' }).collect();
        let len_s = s.len();

        let f0 = s[0] as usize;
        let f1 = s[1] as usize;
        let f2 = s[2] as usize;
        let f = f0 * 52 * 52 + f1 * 52 + f2;

        let t0 = s[len_s - 3] as usize;
        let t1 = s[len_s - 2] as usize;
        let t2 = s[len_s - 1] as usize;
        let t = t0 * 52 * 52 + t1 * 52 + t2;

        edges[t].push(f);
        words.push((f, t));
        counts[f] = 0;
        counts[t] = 0;
    }

    for &(f, _) in words.iter() {
        counts[f] += 1;
    }

    let queue: Vec<_> = counts.iter().enumerate().filter(|&(_, &c)| c == 0).map(|(i, _)| (i, LOSE)).collect();
    let mut queue = std::collections::VecDeque::from(queue);

    // println!("{:?}", counts.iter().enumerate().filter(|&(_, &c)| c != -1).collect::<Vec<_>>());
    // println!("{:?}", queue);

    let mut ans = vec![DRAW; m];

    while let Some((i, a)) = queue.pop_front() {
        if ans[i] != DRAW {
            continue;
        }
        ans[i] = a;
        // println!("{:?}", (i, a));

        if a == WIN {
            for &j in edges[i].iter() {
                counts[j] -= 1;
                if counts[j] == 0 {
                    queue.push_back((j, LOSE));
                }
            }
        }

        if a == LOSE {
            for &j in edges[i].iter() {
                queue.push_back((j, WIN));
            }
        }
    }

    for &(_, t) in words.iter() {
        if ans[t] == DRAW {
            println!("Draw");
        }
        if ans[t] == WIN {
            println!("Aoki");
        }
        if ans[t] == LOSE {
            println!("Takahashi");
        }
    }
}

// abc -> bcd -> cda
// ada -> ada

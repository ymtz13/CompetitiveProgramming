static MOD: i64 = 998244352;
static N: usize = 9;
static M: usize = 20;
static K: usize = 81;

static Z: usize = 1 << 31 - 1;

type Grid = Vec<Vec<i64>>;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s)
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn score(aaa: &Grid) -> i64 {
    let mut s = 0;
    for aa in aaa {
        for a in aa {
            s += (a + MOD) % MOD;
        }
    }
    s
}

fn add(aaa: &mut Grid, sss: &Grid, pos: (usize, usize), sign: i64) {
    let (x0, y0) = pos;
    for dx in 0..3 {
        for dy in 0..3 {
            let x = x0 + dx;
            let y = y0 + dy;
            aaa[x][y] += sss[dx][dy] * sign;
            aaa[x][y] += MOD;
            aaa[x][y] %= MOD;
        }
    }
}

fn test(aaa0: &Grid, stamps: &Vec<Grid>, qq: &Vec<(usize, usize, usize)>) -> Grid {
    let mut aaa = aaa0.clone();
    for &(s, x0, y0) in qq {
        add(&mut aaa, &stamps[s], (x0, y0), 1);
    }
    aaa
}

struct Random {
    value: usize,
}

impl Random {
    fn new() -> Self {
        Random { value: 100 }
    }

    fn get(self: &mut Self) -> usize {
        self.value = 48271 * self.value % Z;
        self.value
    }

    fn int(self: &mut Self, r: usize) -> usize {
        self.get() / (Z / r + 1)
    }
}

fn main() {
    read_line();

    let mut rand = Random::new();

    let mut aaa: Grid = (0..N).map(|_| read_vec()).collect();
    let aaa0 = aaa.clone();

    let mut stamps = vec![];
    for _ in 0..M {
        let sss: Grid = (0..3).map(|_| read_vec()).collect();
        stamps.push(sss);
    }

    let mut qq = vec![];
    for _ in 0..K {
        let s = rand.int(M);
        let x0 = rand.int(N - 2);
        let y0 = rand.int(N - 2);
        qq.push((s, x0, y0));

        add(&mut aaa, &stamps[s], (x0, y0), 1);
    }

    let mut score_now = score(&aaa);
    let iteration = 2_000_000;
    // let iteration = 1_000_000;
    // let iteration = 500_000;
    let size = 1;
    for _step in 0..iteration {
        let mut ii: Vec<_> = (0..size).map(|_| rand.int(K)).collect();
        ii.sort();
        ii.dedup();

        let qq_now: Vec<_> = ii.iter().map(|&i| qq[i].clone()).collect();
        let qq_nxt: Vec<_> = ii.iter().map(|_| (rand.int(M), rand.int(N - 2), rand.int(N - 2))).collect();
        for &(s, x0, y0) in &qq_now {
            add(&mut aaa, &stamps[s], (x0, y0), -1);
        }
        for &(s, x0, y0) in &qq_nxt {
            add(&mut aaa, &stamps[s], (x0, y0), 1);
        }

        let score_nxt = score(&aaa);

        if score_nxt >= score_now {
            if score_nxt > score_now {
                println!("({}) {} -> {}", _step, score_now, score_nxt);
            }
            score_now = score_nxt;
            for (&i, &q) in ii.iter().zip(qq_nxt.iter()) {
                qq[i] = q;
            }
        } else {
            for &(s, x0, y0) in &qq_nxt {
                add(&mut aaa, &stamps[s], (x0, y0), -1);
            }
            for &(s, x0, y0) in &qq_now {
                add(&mut aaa, &stamps[s], (x0, y0), 1);
            }
        }
    }

    // let aaa_test = test(&aaa0, &stamps, &qq);
    // let eq = aaa.iter().eq(aaa_test.iter());
    // println!("{}", eq);

    println!("{}", K);
    for (s, x0, y0) in &qq {
        println!("{} {} {}", s, x0, y0);
    }
}

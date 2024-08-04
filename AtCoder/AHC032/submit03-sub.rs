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
    fn new(seed: usize) -> Self {
        let mut rand = Random { value: seed };
        for _ in 0..10 {
            rand.get();
        }
        rand
    }

    fn get(self: &mut Self) -> usize {
        self.value = 48271 * self.value % Z;
        self.value
    }

    fn int(self: &mut Self, r: usize) -> usize {
        self.get() / (Z / r + 1)
    }
}

fn solve(aaa0: &Grid, stamps: &Vec<Grid>, seed: usize) -> (i64, Vec<(usize, usize, usize)>) {
    let mut aaa = aaa0.clone();
    let mut rand = Random::new(seed);

    let mut qq = vec![];
    for _ in 0..K {
        let s = rand.int(M);
        let x0 = rand.int(N - 2);
        let y0 = rand.int(N - 2);
        qq.push((s, x0, y0));

        add(&mut aaa, &stamps[s], (x0, y0), 1);
    }

    let mut score_now = score(&aaa);
    let iteration = 800_000;
    for _step in 0..iteration {
        let i = rand.int(K);
        let q_now = qq[i];
        let q_nxt = (rand.int(M), rand.int(N - 2), rand.int(N - 2));

        {
            let (s, x0, y0) = q_now;
            add(&mut aaa, &stamps[s], (x0, y0), -1);
        }
        {
            let (s, x0, y0) = q_nxt;
            add(&mut aaa, &stamps[s], (x0, y0), 1);
        }

        let score_nxt = score(&aaa);

        if score_nxt >= score_now {
            score_now = score_nxt;
            qq[i] = q_nxt;
        } else {
            {
                let (s, x0, y0) = q_nxt;
                add(&mut aaa, &stamps[s], (x0, y0), -1);
            }
            {
                let (s, x0, y0) = q_now;
                add(&mut aaa, &stamps[s], (x0, y0), 1);
            }
        }
    }

    (score_now, qq)
}

fn main() {
    read_line();

    let mut rand = Random::new(100);

    let aaa0: Grid = (0..N).map(|_| read_vec()).collect();

    let mut stamps = vec![];
    for _ in 0..M {
        let sss: Grid = (0..3).map(|_| read_vec()).collect();
        stamps.push(sss);
    }

    let ss: Vec<_> = (1..=10).map(|seed| solve(&aaa0, &stamps, seed)).collect();

    let max = ss.iter().max_by_key(|(s, _)| s).unwrap();

    // println!("{:?}", ss);
    // println!("{:?}", max);

    println!("{}", K);
    for (s, x0, y0) in &(max.1) {
        println!("{} {} {}", s, x0, y0);
    }
}

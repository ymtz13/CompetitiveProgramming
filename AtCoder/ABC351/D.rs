fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let hw: Vec<usize> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let h = hw[0];
    let w = hw[1];

    let mut sss = vec![];
    for _ in 0..h {
        sss.push(read_line().into_bytes());
    }

    for ih in 0..h {
        for iw in 0..w {
            if sss[ih][iw] != b'.' {
                continue;
            }

            if ih > 0 && sss[ih - 1][iw] == b'#' {
                sss[ih][iw] = b'_';
            }
            if ih < h - 1 && sss[ih + 1][iw] == b'#' {
                sss[ih][iw] = b'_';
            }
            if iw > 0 && sss[ih][iw - 1] == b'#' {
                sss[ih][iw] = b'_';
            }
            if iw < w - 1 && sss[ih][iw + 1] == b'#' {
                sss[ih][iw] = b'_';
            }
        }
    }

    let z = h * w;
    let mut visited = vec![vec![z; w]; h];
    let mut ans = 1;

    for sh in 0..h {
        for sw in 0..w {
            let i = sh * w + sw;

            if sss[sh][sw] != b'.' || visited[sh][sw] != z {
                continue;
            }

            let mut cnt = 0;
            let mut queue = std::collections::VecDeque::from(vec![(sh, sw)]);

            while let Some((ih, iw)) = queue.pop_front() {
                if visited[ih][iw] == i {
                    continue;
                }
                visited[ih][iw] = i;
                cnt += 1;

                if sss[ih][iw] == b'_' {
                    continue;
                }

                if ih > 0 {
                    queue.push_back((ih - 1, iw));
                }
                if ih < h - 1 {
                    queue.push_back((ih + 1, iw));
                }
                if iw > 0 {
                    queue.push_back((ih, iw - 1));
                }
                if iw < w - 1 {
                    queue.push_back((ih, iw + 1));
                }
            }

            if cnt > ans {
                ans = cnt;
            }
        }
    }

    println!("{ans}");
}

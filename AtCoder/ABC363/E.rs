fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

use std::collections::BinaryHeap;

fn main() {
    let (h, w, y) = read_uuu();
    let mut aaa = vec![];
    for _ in 0..h {
        let aa = read_vec();
        aaa.push(aa);
    }

    let mut heap = BinaryHeap::new();
    for iw in 0..w {
        heap.push((-(aaa[0][iw] as i64), 0, iw));
        aaa[0][iw] = 0;
        if h > 1 {
            heap.push((-(aaa[h - 1][iw] as i64), h - 1, iw));
            aaa[h - 1][iw] = 0;
        }
    }

    for ih in 1..h - 1 {
        heap.push((-(aaa[ih][0] as i64), ih, 0));
        aaa[ih][0] = 0;
        if w > 1 {
            heap.push((-(aaa[ih][w - 1] as i64), ih, w - 1));
            aaa[ih][w - 1] = 0;
        }
    }

    let mut ans = h * w;

    for i in 1..=y {
        let i = i as i64;

        while let Some((a, ih, iw)) = heap.pop() {
            let a = -a;
            if a > i {
                heap.push((-a, ih, iw));
                break;
            }

            ans -= 1;

            if ih > 0 {
                let (jh, jw) = (ih - 1, iw);
                if aaa[jh][jw] != 0 {
                    heap.push((-(aaa[jh][jw] as i64), jh, jw));
                    aaa[jh][jw] = 0;
                }
            }

            if ih < h - 1 {
                let (jh, jw) = (ih + 1, iw);
                if aaa[jh][jw] != 0 {
                    heap.push((-(aaa[jh][jw] as i64), jh, jw));
                    aaa[jh][jw] = 0;
                }
            }

            if iw > 0 {
                let (jh, jw) = (ih, iw - 1);
                if aaa[jh][jw] != 0 {
                    heap.push((-(aaa[jh][jw] as i64), jh, jw));
                    aaa[jh][jw] = 0;
                }
            }

            if iw < w - 1 {
                let (jh, jw) = (ih, iw + 1);
                if aaa[jh][jw] != 0 {
                    heap.push((-(aaa[jh][jw] as i64), jh, jw));
                    aaa[jh][jw] = 0;
                }
            }
        }

        println!("{ans}");
    }
}

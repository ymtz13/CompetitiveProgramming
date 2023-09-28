use std::collections::BTreeSet;

fn main() {
  let mut inp = String::new();
  std::io::stdin().read_line(&mut inp).unwrap();

  let wh: Vec<u64> = inp.split_whitespace().map(|c| c.parse().unwrap()).collect();
  let w = wh[0];
  let h = wh[1];

  inp.clear();
  std::io::stdin().read_line(&mut inp).unwrap();
  let n: u64 = inp.trim().parse().unwrap();

  let mut bvec = Vec::new();
  let mut sx = BTreeSet::new();
  let mut sy = BTreeSet::new();
  sx.insert(0);
  sx.insert(w+1);
  sy.insert(0);
  sy.insert(h+1);

  for _ in 0..n {
    inp.clear();
    std::io::stdin().read_line(&mut inp).unwrap();
    let v: Vec<u64> = inp.split_whitespace().map(|c| c.parse().unwrap()).collect();
    let x1 = v[0] + 1;
    let y1 = v[1] + 1;
    let x2 = v[2] + 1;
    let y2 = v[3] + 1;

    sx.insert(x1);
    sx.insert(x2);
    sy.insert(y1);
    sy.insert(y2);

    bvec.push((x1, y1, x2, y2));
  }


  println!("{:?}", (w, h, n, bvec, sx, sy));

}
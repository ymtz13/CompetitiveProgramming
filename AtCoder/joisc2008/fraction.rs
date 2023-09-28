use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Debug, Eq, Clone, Copy)]
struct F {
  n: u64,
  d: u64,
}

impl F {
  fn reduce(&self) -> F {
    let mut a = self.n;
    let mut b = self.d;
    while a%b != 0 {
      let tmp = a;
      a = b;
      b = tmp%b;
    }
    
    F{n:self.n/b, d:self.d/b}
  }
}

impl PartialEq for F {
  fn eq(&self, other: &Self) -> bool {
    self.cmp(other) == Ordering::Equal
  }
}

impl Ord for F {
  fn cmp(&self, other: &Self) -> Ordering {
    (other.n * self.d).cmp(&(self.n * other.d))
  }
}

impl PartialOrd for F {
  fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
      Some(self.cmp(other))
  }
}

fn main() {
  let mut inp = String::new();
  std::io::stdin().read_line(&mut inp).unwrap();

  let a: Vec<u64> = inp.trim().split_whitespace().map(|c| c.parse().unwrap()).collect();

  let m = a[0];
  let k = a[1];

  let mut heap = BinaryHeap::new();

  for d in 2..=m {
    heap.push(F{n:1, d});
  }

  let mut prev = F{n:0, d:1};
  let mut cnt = 0;
  while let Some(f) = heap.pop() {
    if f != prev {
      prev = f;
      cnt+=1;
      if cnt == k {
        let rf = f.reduce();
        println!("{} {}", rf.n, rf.d);
        std::process::exit(0);
      }
    }

    if f.n + 1 < f.d {
      heap.push(F{n: f.n+1, d:f.d});
    }
  }

  println!("-1");

}
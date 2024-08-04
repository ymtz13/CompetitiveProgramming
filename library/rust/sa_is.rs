const UNDEFINED: usize = usize::MAX;

#[derive(PartialEq, Debug, Clone, Copy)]
enum LS {
    L,
    S,
}

fn induced_sort(n: usize, k: usize, aa: &Vec<usize>, ls: &Vec<LS>, bin: &Vec<usize>, lms: &Vec<usize>) -> Vec<usize> {
    let mut sa = vec![UNDEFINED; n];

    let mut bincnt = vec![0; k];
    for &i in lms.iter().rev() {
        let a = aa[i];
        sa[bin[a + 1] - 1 - bincnt[a]] = i;
        bincnt[a] += 1;
    }

    // println!("sa1: {sa:?}");

    let mut bincnt = vec![0; k];
    for p in 0..n {
        let i = sa[p];
        if i == UNDEFINED || i == 0 || ls[i - 1] == LS::S {
            continue;
        }

        let a = aa[i - 1];
        sa[bin[a] + bincnt[a]] = i - 1;
        bincnt[a] += 1;
    }

    // println!("sa2: {sa:?}");

    let mut bincnt = vec![0; k];
    for p in (0..n).rev() {
        let i = sa[p];
        if i == UNDEFINED || i == 0 || ls[i - 1] == LS::L {
            continue;
        }

        let a = aa[i - 1];
        sa[bin[a + 1] - 1 - bincnt[a]] = i - 1;
        bincnt[a] += 1;
    }

    // println!("sa3: {sa:?}");

    sa
}

fn sa_is(aa: &Vec<usize>) -> Vec<usize> {
    use std::collections::{BTreeSet, HashMap};

    if aa.len() == 0 {
        return vec![0];
    }

    if aa.len() == 1 {
        return vec![1, 0];
    }

    let char_set: BTreeSet<_> = aa.iter().cloned().collect();
    let char_map: HashMap<usize, usize> = char_set.iter().cloned().enumerate().map(|(i, v)| (v, i + 1)).collect();
    let aa: Vec<_> = aa.iter().map(|a| *char_map.get(a).unwrap()).chain(std::iter::once(0)).collect();

    let n = aa.len();
    let k = char_map.len() + 1;

    let mut cnt = vec![0; k];
    for &a in &aa {
        cnt[a] += 1;
    }

    let mut bin = vec![0];
    for &c in &cnt {
        bin.push(bin.last().unwrap() + c);
    }
    // println!("cnt: {cnt:?}");
    // println!("bin: {bin:?}");

    let mut ls = vec![LS::S; n];
    for i in (0..n - 1).rev() {
        if aa[i] > aa[i + 1] {
            ls[i] = LS::L;
        }
        if aa[i] == aa[i + 1] {
            ls[i] = ls[i + 1];
        }
    }
    // println!("ls : {ls:?}");

    let mut lms_idx = vec![UNDEFINED; n];
    let mut lms = vec![];
    for i in 1..=n {
        if ls[i - 1] == LS::L && ls[i] == LS::S {
            lms_idx[i] = lms.len();
            lms.push(i);
        }
    }
    // println!("lms: {lms:?}");
    // println!("idx: {lms_idx:?}");

    let sa = induced_sort(n, k, &aa, &ls, &bin, &lms);

    let mut compressed = vec![0; lms.len()];
    let mut cnt_substr = 0;
    let mut l_prv = n - 1;
    let mut r_prv = n - 1;
    for p in 1..n {
        let l = sa[p];
        if lms_idx[l] != UNDEFINED {
            let r = lms[lms_idx[l] + 1];

            if &aa[l..=r] != &aa[l_prv..=r_prv] {
                cnt_substr += 1;
                l_prv = l;
                r_prv = r;
            }

            compressed[lms_idx[l]] = cnt_substr;
        }
    }

    // println!("cmp:{compressed:?}");

    let sa_compressed = sa_is(&compressed);
    let lms_ordered: Vec<_> = sa_compressed[1..].iter().map(|&p| lms[p]).collect();
    // println!("lms_ordered:{lms_ordered:?}");

    let sa = induced_sort(n, k, &aa, &ls, &bin, &lms_ordered);
    sa
}

fn main() {
    let aa = String::from("mmiissiissiippii").bytes().map(|c| c as usize).collect();
    let sa = sa_is(&aa);

    println!("{sa:?}");
}

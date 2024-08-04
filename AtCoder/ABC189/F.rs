fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let nmk = read_vec();
    let n = nmk[0];
    let m = nmk[1];
    // let k = nmk[2];

    let aa = read_vec();
    let aa: std::collections::HashSet<_> = aa.iter().collect();

    let mf = m as f64;

    let mut dp_pr = vec![0.0; n + m];
    let mut dp_ep = vec![0.0; n + m];
    let mut dp_ex = vec![0.0; n + m];
    let mut acc_pr = vec![0.0, 1.0];
    let mut acc_ep = vec![0.0, 0.0];
    dp_pr[0] = 1.0;

    for t in 1..n + m {
        let s_pr = acc_pr[std::cmp::min(t, n)] - acc_pr[if t >= m { t - m } else { 0 }];
        let s_ep = acc_ep[std::cmp::min(t, n)] - acc_ep[if t >= m { t - m } else { 0 }];

        dp_pr[t] = s_pr / mf;
        dp_ex[t] = if s_pr > 0.0 { s_ep / s_pr + 1.0 } else { 0.0 };
        dp_ep[t] = dp_pr[t] * dp_ex[t];

        if aa.contains(&t) {
            acc_pr.push(acc_pr[t]);
            acc_ep.push(acc_ep[t]);
        } else {
            acc_pr.push(acc_pr[t] + dp_pr[t]);
            acc_ep.push(acc_ep[t] + dp_ep[t]);
        }
    }

    // eprintln!("{:?}", dp_pr);
    // eprintln!("{:?}", dp_ex);
    // eprintln!("{:?}", dp_ep);

    let mut pr_goal = 0.0;
    let mut ep_goal = 0.0;
    for i in n..n + m {
        pr_goal += dp_pr[i];
        ep_goal += dp_ep[i];
    }
    // eprintln!("{:?}", (pr_goal, 1.0 - pr_goal));

    let pr_reset = 1.0 - pr_goal;
    let mut ep_reset = 0.0;
    for &i in aa.iter() {
        ep_reset += dp_ep[*i];
    }

    if pr_goal == 0.0 {
        println!("-1");
    } else {
        if pr_reset == 0.0 {
            println!("{}", ep_goal);
        } else {
            let ex_goal = ep_goal / pr_goal;
            let ex_reset = ep_reset / pr_reset;
            let ans = ex_reset * pr_reset / pr_goal + ex_goal;
            println!("{}", ans);
        }
    }
}

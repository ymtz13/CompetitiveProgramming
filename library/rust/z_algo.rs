fn z_algo<T: std::cmp::PartialEq>(arr: &Vec<T>) -> Vec<usize> {
    let l = arr.len();
    let mut ret = vec![l];
    let mut i = 1;
    let mut jnxt = 0;
    while i < l {
        let mut j = jnxt;
        while i + j < l && arr[j] == arr[i + j] {
            j += 1;
        }

        ret.push(j);

        jnxt = 0;
        for k in 1..=j {
            if k + ret[k] >= j {
                jnxt = j - k;
                break;
            }
            ret.push(ret[k]);
        }

        i = ret.len();
    }

    ret
}

fn main() {
    let res = z_algo(&"010101_0_010101".bytes().collect());
    println!("{:?}", res);
}

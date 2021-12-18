#![allow(dead_code)]
#![allow(unused_variables)]
use regex::Regex;

#[inline]
pub fn main() {
    let reg = Regex::new(r"-?\d+").unwrap();
    let target: Vec<i32> = reg
        .captures_iter(&include_str!("../input.txt"))
        .map(|x| x.get(0).unwrap().as_str().parse().unwrap())
        .collect();
    let (a, b) = launch_prob(target);
}

fn launch_prob(target: Vec<i32>) -> (i32, Vec<i32>) {
    let [x1, x2, y1, y2] = <[i32; 4]>::try_from(target).ok().unwrap();
    let mut acc = 0;
    let mut maxy = Vec::new();
    for i in 1..x2 + 1 {
        for j in y1..-y1 {
            let mut hor = i;
            let mut ver = j;
            let mut hy = 0;
            let mut x = 0;
            let mut y = 0;
            while !(x <= x2 && x >= x1 && y >= y1 && y <= y2) {
                let py = y;
                x += hor;
                y += ver;
                if py > y && hy == 0 {
                    hy = py;
                };
                ver -= 1;
                if hor < 0 {
                    hor += 1;
                } else if hor > 0 {
                    hor -= 1;
                } else {
                    hor = 0;
                }
                if x >= x2 || y <= y1 {
                    break;
                }
            }
            if x <= x2 && x >= x1 && y >= y1 && y <= y2 {
                acc += 1;
                maxy.push(hy);
            }
        }
    }
    return (acc, maxy);
}

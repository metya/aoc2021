#![allow(dead_code)]
#![allow(unused_variables)]
use ::counter::Counter;
use ::std::collections::HashMap;

#[inline]
pub fn solve_p() {
    let input: Vec<&str> = include_str!("../input.txt").lines().collect();
    let example: Vec<&str> = include_str!("../example.txt").lines().collect();
    let canonical_pattern = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg";
    let counter = canonical_pattern.chars().collect::<Counter<_>>();
    let wires: HashMap<_, _> = canonical_pattern
        .split_ascii_whitespace()
        .enumerate()
        .map(|(ind, code)| (get_key(&code, &counter), ind))
        .collect();

    let part1 = input
        .iter()
        .map(|line| {
            line.split_once("|")
                .map(|(left, right)| {
                    right
                        .split_ascii_whitespace()
                        .fold(0, |acc, code| match code.chars().count() {
                            2 | 3 | 4 | 7 => acc + 1,
                            _ => acc,
                        })
                })
                .unwrap()
        })
        .sum::<usize>();

    let part2 = input
        .iter()
        .map(|line| {
            line.split_once("|")
                .map(|(left, right)| {
                    let occurence = left.chars().collect::<Counter<_>>();
                    right
                        .split_ascii_whitespace()
                        .fold(String::new(), |st, code| {
                            st + &wires[&get_key(&code, &occurence)].to_string()
                        })
                        .parse::<usize>()
                        .unwrap()
                })
                .unwrap()
        })
        .sum::<usize>();
}

fn get_key(code: &str, counter: &Counter<char>) -> usize {
    code.chars().map(|ch| counter[&ch]).sum::<usize>()
}

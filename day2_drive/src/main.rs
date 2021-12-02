#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {
    let instructions: Vec<&str> = include_str!("../input.txt").lines().collect();
    let example: Vec<&str> = include_str!("../example.txt").lines().collect();
    check_example(&example, &part1);
    part1(&instructions);
    check_example(&example, &part2);
    part2(&instructions);
}

fn check_example(example: &Vec<&str>, part: &dyn Fn(&Vec<&str>)) {
    part(&example)
}

fn part1(input: &Vec<&str>) {
    let (forward, depth) =
        input
            .iter()
            .fold((0, 0), |(f, d), line| match line.split_once(" ").unwrap() {
                ("forward", v) => (f + v.parse::<i32>().unwrap(), d),
                ("down", v) => (f, d + v.parse::<i32>().unwrap()),
                ("up", v) => (f, d - v.parse::<i32>().unwrap()),
                _ => (f, d),
            });
    println!("The answer of part1 is: {}", depth * forward);
}

fn part2(input: &Vec<&str>) {
    let (forward, depth, _) = input.iter().fold((0, 0, 0), |(f, d, a), line| {
        match line.split_once(" ").unwrap() {
            ("forward", v) => (
                f + v.parse::<i32>().unwrap(),
                d + a * v.parse::<i32>().unwrap(),
                a,
            ),
            ("down", v) => (f, d, a + v.parse::<i32>().unwrap()),
            ("up", v) => (f, d, a - v.parse::<i32>().unwrap()),
            _ => (f, d, a),
        }
    });
    println!("The answer of part2 is: {}", depth * forward);
}

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

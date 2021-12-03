fn main() {
    let measures: Vec<i32> = include_str!("../input.txt")
        .lines()
        .map(|x| x.parse().unwrap())
        .collect();
    let example: Vec<i32> = include_str!("../example.txt")
        .lines()
        .map(|x| x.parse().unwrap())
        .collect();

    check_example(&example, &part1);
    check_example(&example, &part2);
    part1(&measures);
    part2(&measures);
}

fn check_example(example: &Vec<i32>, part: &dyn Fn(&Vec<i32>)) {
    part(&example)
}

fn part1(input: &Vec<i32>) {
    let mut counter = 0;
    let mut temp = input.iter().max().unwrap();
    for measure in input {
        if measure > temp {
            counter += 1;
        }
        temp = measure
    }
    println!("The Answer of part1 is: {}", counter);
}

fn part2(input: &Vec<i32>) {
    let mut counter = 0;
    // let temp: i32 = input[0..3].iter().sum();
    for ind in 0..(input.len() - 3) {
        if input[ind] < input[ind + 3] {
            // println!("{}, {}, {}", ind, input[ind], input[ind + 3]);
            counter += 1
        }
    }
    println!("The Answer of part2 is: {}", counter);
}

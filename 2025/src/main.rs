use aoc_2025::solve;
use std::fs;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let day: u8 = args[1].parse().unwrap();
    let input =
        fs::read_to_string(format!("inputs/day_{:02}.txt", day)).expect("No input file found");

    let (p1, p2) = solve(day, &input);
    println!("Part 1: {}", p1);
    println!("Part 2: {}", p2);
}

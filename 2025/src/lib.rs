pub mod days;

pub fn solve(day: u8, input: &str) -> (String, String) {
    match day {
        1 => days::day_01::solve(input),
        _ => panic!("Day {} is not implemented", day),
    }
}

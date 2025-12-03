pub fn solve(input: &str) -> (String, String) {
    (part1(input), part2(input))
}

fn part1(input: &str) -> String {
    let lines: Vec<&str> = input.lines().collect();

    let mut pos: i64 = 50;
    let mut count: u64 = 0;

    for line in lines {
        let dir = &line[0..1];
        let dist = &line[1..];
        let abs_dist = dist.parse::<i64>().unwrap() % 100;

        match dir {
            "L" => pos -= abs_dist,
            "R" => pos += abs_dist,
            _ => panic!("Invalid direction {}", dir),
        }

        if pos < 0 {
            pos = 100 + pos;
        } else if pos > 99 {
            pos = pos - 100;
        }

        if pos == 0 {
            count += 1
        }
    }

    return count.to_string();
}

fn part2(input: &str) -> String {
    let lines: Vec<&str> = input.lines().collect();

    let mut pos: i64 = 50;
    let mut count: u64 = 0;

    for line in lines {
        let direction: i64 = if line.chars().next().unwrap() == 'L' {
            -1
        } else {
            1
        };
        let magnitude: i64 = line[1..].parse().unwrap();

        let old_position = pos;
        let new_pos = pos + direction * magnitude;

        let q = new_pos.div_euclid(100);
        let r = new_pos.rem_euclid(100);

        count += q.abs() as u64 + if direction == -1 && r == 0 { 1 } else { 0 }
            - if direction == -1 && old_position == 0 {
                1
            } else {
                0
            };

        pos = r;
    }

    return count.to_string();
}

use std::collections::HashSet;
use std::fs;

fn main() {
    let contents = parse_input("input");
    let ans = part_one(&contents).unwrap();
    let ans2 = part_two(&contents).unwrap();
    println!("part one: {}", ans);
    println!("part two: {}", ans2);
}

fn parse_input(file_path: &str) -> HashSet<i32> {
    fs::read_to_string(file_path)
        .unwrap()
        .trim()
        .split("\n")
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<HashSet<i32>>()
}

fn part_one(contents: &HashSet<i32>) -> Option<i32> {
    for num in contents {
        if contents.contains(&(2020 - num)) {
            return Some((2020 - num) * num);
        }
    }
    None
}

fn part_two(contents: &HashSet<i32>) -> Option<i32> {
    for num in contents {
        for num2 in contents {
            if contents.contains(&(2020 - num - num2)) {
                return Some((2020 - num - num2) * num * num2);
            }
        }
    }
    None
}

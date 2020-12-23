use lazy_static::lazy_static;
use regex::Regex;
use std::fs;

fn main() {
    let parsed = parse_passwords("../input");
    let ans = count_valid(&parsed);
    println!("part one: {}\npart two: {}", ans.0, ans.1);
}

struct PwField {
    low: usize,
    high: usize,
    chr: String,
    pw: String,
}

impl PwField {
    fn new(data: &str) -> Self {
        lazy_static! {
            static ref RE: Regex = Regex::new(r"(\d+)-(\d+) ([a-z])").unwrap();
        }
        let itr = data.split(": ").collect::<Vec<&str>>();
        let caps = RE.captures(itr[0]).unwrap();
        PwField {
            low: caps[1].parse::<usize>().unwrap(),
            high: caps[2].parse::<usize>().unwrap(),
            chr: caps[3].to_string(),
            pw: itr[1].to_string(),
        }
    }

    fn part_one_validation(&self) -> bool {
        let cnt = self.pw.matches(&self.chr).count();
        (self.low..=self.high).contains(&cnt)
    }

    fn part_two_validation(&self) -> bool {
        let pw_bytes = self.pw.as_bytes();
        let chr_byte = self.chr.as_bytes()[0];
        (pw_bytes[self.low - 1] == chr_byte) ^ (pw_bytes[self.high - 1] == chr_byte)
    }
}

fn parse_passwords(database: &str) -> Vec<PwField> {
    fs::read_to_string(database)
        .unwrap()
        .trim()
        .split("\n")
        .map(|x| PwField::new(x))
        .collect::<Vec<_>>()
}

fn count_valid(entries: &Vec<PwField>) -> (u32, u32) {
    let mut valid1: u32 = 0;
    let mut valid2: u32 = 0;
    for entry in entries {
        if entry.part_one_validation() {
            valid1 += 1;
        }
        if entry.part_two_validation() {
            valid2 += 1;
        }
    }
    (valid1, valid2)
}

use lazy_static::lazy_static;
use regex::Regex;
use std::fs;

#[derive(Debug)]
struct Field {
    key: String,
    value: String,
}

impl Field {
    fn new(field: &str) -> Self {
        let tmp: Vec<_> = field.split(":").collect();
        Field {
            key: tmp[0].to_string(),
            value: tmp[1].to_string(),
        }
    }

    fn least_and_most(&self, least: i32, most: i32) -> bool {
        let val: i32 = self.value.parse().unwrap();
        val >= least && val <= most
    }

    fn is_valid(&self) -> bool {
        match &self.key[..] {
            "byr" => self.least_and_most(1920, 2002),
            "iyr" => self.least_and_most(2010, 2020),
            "eyr" => self.least_and_most(2020, 2030),
            "hgt" => {
                lazy_static! {
                    static ref HEIGHTEX: Regex = Regex::new(r"(\d+)(in|cm)").unwrap();
                }
                if let Some(caps) = HEIGHTEX.captures(&self.value) {
                    let height = caps.get(1).unwrap().as_str().parse::<i32>().unwrap();
                    let unit = caps.get(2).unwrap().as_str();
                    if unit == "cm" {
                        height >= 150 && height <= 193
                    } else {
                        height >= 59 && height <= 76
                    }
                } else {
                    false
                }
            }
            "hcl" => {
                lazy_static! {
                    static ref HAIREX: Regex = Regex::new(r"^#[a-f0-9]{6}$").unwrap();
                }
                HAIREX.is_match(&self.value)
            }
            "ecl" => {
                lazy_static! {
                    static ref EYEX: Regex = Regex::new(r"amb|blu|brn|gry|grn|hzl|oth").unwrap();
                }
                EYEX.is_match(&self.value)
            }
            "pid" => {
                lazy_static! {
                    static ref EYEX: Regex = Regex::new(r"^\d{9}$").unwrap();
                }
                EYEX.is_match(&self.value)
            }
            _ => true,
        }
    }
}

#[derive(Debug)]
struct Document {
    fields: Vec<Field>,
}

impl Document {
    fn new(doc: &str) -> Self {
        Document {
            fields: doc
                .split(char::is_whitespace)
                .map(|x| Field::new(x))
                .collect(),
        }
    }

    fn no_cid(&self) -> bool {
        for field in &self.fields {
            if field.key == "cid" {
                return false;
            }
        }
        true
    }

    fn first_validation(&self) -> bool {
        match &self.fields.len() {
            8 => true,
            7 => self.no_cid(),
            _ => false,
        }
    }

    fn second_validation(&self) -> bool {
        for field in &self.fields {
            if !field.is_valid() {
                return false;
            }
        }
        true
    }
}

fn parse_documents(f: &str) -> Vec<Document> {
    fs::read_to_string(f)
        .unwrap()
        .trim()
        .split("\n\n")
        .map(|x| Document::new(x))
        .collect::<Vec<Document>>()
}

fn main() {
    let a = parse_documents("../input");
    let mut part_one: i32 = 0;
    let mut part_two: i32 = 0;
    for doc in &a {
        if doc.first_validation() {
            part_one += 1;
            if doc.second_validation() {
                part_two += 1;
            }
        }
    }
    println!("{}, {}", part_one, part_two);
}

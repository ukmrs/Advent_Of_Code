const OPENING_BRACKETS: [char; 4] = ['(', '[', '{', '<'];

// trait for funzies
trait Bracket {
    fn score(&self) -> i32;
    fn autocomplet_score(&self) -> u64;
    fn to_closing_bracket(&self) -> char;
}

impl Bracket for char {
    fn score(&self) -> i32 {
        match self {
            ')' => 3,
            ']' => 57,
            '}' => 1197,
            '>' => 25137,
            _ => unreachable!(),
        }
    }

    fn to_closing_bracket(&self) -> char {
        match self {
            '(' => ')',
            '[' => ']',
            '{' => '}',
            '<' => '>',
            _ => unreachable!(),
        }
    }

    fn autocomplet_score(&self) -> u64 {
        match self {
            '(' => 1,
            '[' => 2,
            '{' => 3,
            '<' => 4,
            _ => unreachable!(),
        }
    }
}

// ponder the orb
fn consider_line(line: &str, stack: &mut Vec<char>) -> Option<i32> {
    for c in line.chars() {
        if OPENING_BRACKETS.contains(&c) {
            stack.push(c);
        } else {
            let bracket = stack.pop().unwrap();
            let corresponding = bracket.to_closing_bracket();
            if corresponding != c {
                return Some(c.score());
            }
        }
    }
    None
}

fn solve(input: &str) -> i32 {
    let mut stack: Vec<char> = vec![];
    let mut count = 0;
    for line in input.lines() {
        count += consider_line(line, &mut stack).unwrap_or(0);
        stack.clear();
    }
    count
}

fn solve_two(input: &str) -> u64 {
    let mut stack: Vec<char> = vec![];
    let mut scores: Vec<u64> = vec![];
    for line in input.lines() {
        if consider_line(line, &mut stack).is_some() {
            stack.clear();
            continue;
        };

        let mut score = 0;
        loop {
            if let Some(bracket) = stack.pop() {
                score *= 5;
                score += bracket.autocomplet_score();
            } else {
                scores.push(score);
                break;
            }
        }
    }
    scores.sort_unstable();
    scores[scores.len() / 2]
}

fn main() {
    let ex = include_str!("./example");
    let inp = include_str!("./input");
    assert_eq!(solve(ex), 26397);
    assert_eq!(solve_two(ex), 288957);

    let ans = solve(inp);
    let ans_two = solve_two(inp);
    println!("{}", ans);
    println!("{}", ans_two);
}

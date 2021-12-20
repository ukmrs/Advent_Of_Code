const DIRECTIONS: [(isize, isize); 8] = [
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (-1, -1),
    (1, 1),
];

// Another dumb trait, because i can
// you want to stop me?
// it is too late you know;
//
// Better use of your time would be to lookup these things
// if you haven't already
// they are very cool
// up there with capybaras for sure
trait DumboOctopus {
    fn flash(&mut self, x: usize, y: usize);
    fn increment(&mut self);
}

impl DumboOctopus for Vec<Vec<i32>> {
    fn increment(&mut self) {
        for row in self {
            for cell in row {
                *cell += 1;
            }
        }
    }

    fn flash(&mut self, x: usize, y: usize) {
        self[y][x] = -420;
        let ox = x as isize;
        let oy = y as isize;

        for (dx, dy) in &DIRECTIONS {
            let x = ox - dx;
            let y = oy - dy;

            if x >= 0 && y >= 0 && self.len() > x as usize && self[0].len() > y as usize {
                self[y as usize][x as usize] += 1;
            }
        }
    }
}

fn to_2d(input: &str) -> Vec<Vec<i32>> {
    input
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap() as i32)
                .collect()
        })
        .collect()
}

enum Part {
    One,
    Two,
}

fn solve(input: &str, steps: i32, part: Part) -> i32 {
    let mut array = to_2d(input);
    let rowlen = array.len();
    let collen = array[0].len();
    let mut flashed = false;
    let mut synchronized: bool;
    let mut count = 0;
    let mut synchronized_step = 0;

    for step in 0..steps {
        array.increment();

        loop {
            for y in 0..rowlen {
                for x in 0..collen {
                    if array[y][x] > 9 {
                        array.flash(x, y);
                        flashed = true;
                        count += 1;
                    }
                }
            }

            if !flashed {
                break;
            }

            flashed = false;
        }

        synchronized = true;
        for y in 0..rowlen {
            for x in 0..collen {
                if array[y][x] < 0 {
                    array[y][x] = 0;
                } else {
                    synchronized = false;
                }
            }
        }

        if synchronized && matches!(part, Part::Two) {
            synchronized_step = step + 1;
            break;
        }
    }

    match part {
        Part::One => count,
        Part::Two => synchronized_step,
    }
}

fn main() {
    let ex = include_str!("./example");
    let inp = include_str!("./input");
    assert_eq!(solve(ex, 10, Part::One), 204);
    assert_eq!(solve(ex, 100, Part::One), 1656);
    assert_eq!(solve(ex, i32::MAX, Part::Two), 195);

    let one_ans = solve(inp, 100, Part::One);
    let two_ans = solve(inp, i32::MAX, Part::Two);
    println!("{}", one_ans);
    println!("{}", two_ans);
}

use std::collections::VecDeque;

fn to_2d(unparsed: &str) -> Vec<Vec<u32>> {
    unparsed
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<u32>>()
        })
        .collect()
}

fn is_out_of_bounds(n: i32, bound: i32) -> bool {
    n < 0 || n >= bound
}

fn solve(input: &str) -> u32 {
    let array = to_2d(input);

    let mut count = 0;
    let mut bigger: bool;
    let rowlen = array.len();
    let collen = array[0].len();
    let delta = [(-1, 0), (0, -1), (1, 0), (0, 1)];

    for row in 0..rowlen {
        for col in 0..collen {
            bigger = false;
            let x = array[row][col];

            for (dy, dx) in &delta {
                let a = row as i32 + dy;
                let b = col as i32 + dx;

                if is_out_of_bounds(a, rowlen as i32) || is_out_of_bounds(b, collen as i32) {
                    continue;
                }

                if x >= array[a as usize][b as usize] {
                    bigger = true;
                    break;
                }
            }

            if !bigger {
                count += x + 1;
            }
        }
    }
    count
}

#[derive(Debug)]
struct Coordinate {
    x: usize,
    y: usize,
}

fn get_min_with_index(arr: &[i32]) -> (i32, usize) {
    let mut min_num = arr[0];
    let mut min_ix = 0_usize;
    for (ix, num) in arr.iter().enumerate() {
        if min_num > *num {
            min_num = *num;
            min_ix = ix
        }
    }
    (min_num, min_ix)
}

fn solve_two(input: &str) -> i32 {
    let mut array = to_2d(input);
    let rowlen = array.len();
    let collen = array[0].len();
    let mut ans = [0; 3];

    let mut que: VecDeque<Coordinate> = VecDeque::new();
    for y in 0..rowlen {
        for x in 0..collen {
            if array[y][x] != 9 {
                que.push_back(Coordinate { x, y })
            }

            let mut count = 0;

            loop {
                if let Some(c) = que.pop_front() {
                    count += 1;
                    array[c.y][c.x] = 9;

                    // quick copypaste because its late XD
                    if c.y + 1 < rowlen && array[c.y + 1][c.x] != 9 {
                        array[c.y + 1][c.x] = 9;
                        que.push_back(Coordinate { y: c.y + 1, x: c.x })
                    }

                    if c.y > 0 && array[c.y - 1][c.x] != 9 {
                        array[c.y - 1][c.x] = 9;
                        que.push_back(Coordinate { y: c.y - 1, x: c.x })
                    }

                    if c.x + 1 < collen && array[c.y][c.x + 1] != 9 {
                        array[c.y][c.x + 1] = 9;
                        que.push_back(Coordinate { y: c.y, x: c.x + 1 })
                    }

                    if c.x > 0 && array[c.y][c.x - 1] != 9 {
                        array[c.y][c.x - 1] = 9;
                        que.push_back(Coordinate { y: c.y, x: c.x - 1 })
                    }
                } else {
                    let (mn, ix) = get_min_with_index(&ans);
                    if count > mn {
                        ans[ix] = count
                    }

                    break;
                }
            }
        }
    }

    ans.iter().product()
}

fn main() {
    let ex = include_str!("./example");
    let ans1 = solve(ex);
    let ans2 = solve_two(ex);
    assert_eq!(ans1, 15);
    assert_eq!(ans2, 1134);

    let inp = include_str!("./input");
    let ans1 = solve(inp);
    let ans2 = solve_two(inp);
    println!("{}\n{}", ans1, ans2);
}

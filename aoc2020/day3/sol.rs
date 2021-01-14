use std::fs;

fn main() {
    let weird_biome = parse_biome("./input");
    let one = toboggan(&weird_biome, 3, 1);
    let two: u64 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        .iter()
        .map(|x| toboggan(&weird_biome, x.0, x.1))
        .product();

    println!("one: {}", one); // 195
    println!("two: {}", two); // 377231400
}

fn toboggan(biome: &Vec<Vec<char>>, right: usize, down: usize) -> u64 {
    let (mut d, mut r, mut trees) = (0, 0, 0);
    let wrap = biome[0].len();
    let height = biome.len();

    while d < height - down {
        d += down;
        r = (r + right) % wrap;
        if biome[d][r] == '#' {
            trees += 1;
        }
    }
    trees
}

fn parse_biome(input: &str) -> Vec<Vec<char>> {
    fs::read_to_string(input)
        .unwrap()
        .trim()
        .split('\n')
        .map(|x| x.trim().chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>()
}

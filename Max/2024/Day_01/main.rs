use std::fs;

fn main()
{
    println!("<<< This is Day 01 / 2024 >>>");

    let mut file_path = "../../../Input/Control/2024/Day_01.txt";
    file_path = "../../../Input/Max/2024/Day_01.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Error regarding read_to_string");

    let mut list_left = Vec::new();
    let mut list_right = Vec::new();

    let mut dist_sum = 0;
    let mut count_num = 0;
    let mut sim_score = 0;

    for line in contents.trim().lines() {
        let numbers: Vec<i32> = line
            .split_whitespace()
            .filter_map(|s| s.parse::<i32>().ok())
            .collect();
        //println!("{:?}", numbers);

        list_left.push(numbers[0]);
        list_right.push(numbers[1]);
    }

    list_left.sort();
    list_right.sort();

    for (index, num_left) in list_left.iter().enumerate()
    {
        dist_sum += (list_left[index] - list_right[index]).abs();

        for num_right in &list_right
        {
            if true == (num_left == num_right)
            {
                count_num += 1;
            }
            else if true == (num_left < num_right)
            {
                break;
            }
        }

        sim_score += num_left * count_num;
        count_num = 0;
    }

    println!("Sum of the distances: {}", dist_sum);
    println!("Similiarity score: {}", sim_score);
}

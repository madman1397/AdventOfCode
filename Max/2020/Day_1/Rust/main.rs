use std::fs;

fn main()
{
    println!("<<< This is Day 01 >>>");

    let file_path = "../../../../Input/Control/2020/Day_01.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q04_p1.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Error regarding read_to_string");

   
    let rows = contents.split("\n").collect::<Vec<_>>();
    let row_len = rows.len();
    let column_len = &rows[0].chars().collect::<Vec<_>>().len();

    let mut matrix: Vec<Vec<char>> = Vec::with_capacity(row_len);

    //<<< create matrix >>>
    for i in 0..(row_len)
    {
        matrix.push(rows[i].chars().collect::<Vec<_>>());
    }

    //print_matrix(&matrix);

    for i in 0..(row_len)
    {
        let read_str = rows[i].to_string();
        let read_int = read_str.parse::<i32>().unwrap();
        println!("{}", read_int);
    }
}

fn print_matrix(matrix: & Vec<Vec<char>>)
{
    let row_len = matrix.len();
    let column_len = matrix[0].len();

    //<<< print matrix >>>
    for i in 0..(row_len)
    {
        for j in 0..(column_len-1)
        {
            print!("{}", matrix[i][j]);
        }
        println!("");
    }
}
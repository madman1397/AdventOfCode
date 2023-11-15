use std::{io, cmp::Ordering};
use rand::Rng;

const CMP_EQUAL: i32 = 0;
const CMP_SMALLER: i32 = 0;
const CMP_GREATER: i32 = 0;

fn main() 
{   
    println!("Hello, world!");

    println!("Guess the number!");
    println!("Please input your guess");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    
    println!("You guessed: {guess}");
}

pub fn compare_equal(value_1 :i32, value_2 :i32) -> bool
{
    match value_1.cmp(&value_2)
    {
        Ordering::Less => return false,
        Ordering::Greater => return false,
        Ordering::Equal => return true,
    }
}

pub fn compare_size(value_is :i32, value_than :i32) -> i32
{
    match value_is.cmp(&value_than)
    {
        Ordering::Less => return CMP_SMALLER,
        Ordering::Greater => return CMP_GREATER,
        Ordering::Equal => return CMP_EQUAL,
    }
}

pub fn rand_num() -> i32
{
    return rand::thread_rng().gen_range(1..=100);
}

#[cfg(test)]
mod tests
{
    use super::*;

    #[test]
    fn test_rand_num()
    {
        for _i in 1..1000000
        {
            if rand_num() > 100 
            {
                assert!(false);
            }
        }
        assert!(true);
    }

    #[test]
    fn test_compare_equal()
    {
        assert_eq!(compare_equal(1, 1), true);
        assert_eq!(compare_equal(1, 2), false);
        assert_eq!(compare_equal(2, 1), false);
    }

    #[test]
    fn test_compare_size()
    {
        assert_eq!(compare_size(1,1), CMP_EQUAL);
        assert_eq!(compare_size(1,2), CMP_SMALLER);
        assert_eq!(compare_size(2,1), CMP_GREATER);
    }
}

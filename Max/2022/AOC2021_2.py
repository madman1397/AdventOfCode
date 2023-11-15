import os

# Initialize the horizontal position and depth to 0
horizontal_position = 0
depth = 0

# Define the planned course as a list of instructions
planned_course = open('Source\M_AOC2021_1.txt')

# Loop through the instructions in the planned course
for instruction in planned_course:
    # Split the instruction into a command and a number
    command, number = instruction.split()

    # Check the command and update the horizontal position and depth accordingly
    if command == "forward":
        horizontal_position += int(number)
    elif command == "down":
        depth += int(number)
    elif command == "up":
        depth -= int(number)

# Print the final horizontal position and depth
print("Final horizontal position:", horizontal_position)
print("Final depth:", depth)

# Multiply the final horizontal position by the final depth to get the answer
answer = horizontal_position * depth
print("Answer:", answer)
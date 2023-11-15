import os
import time
from datetime import timedelta

move_list = list(open('Source\M_AOC2022_9 copy.txt'))
unique_matrix = []

def move_splitter(move_list):
    
    for idx in range(len(move_list)):
        move_list[idx], discard = move_list[idx].split('\n')
        move_list[idx] = move_list[idx].split(' ')

    return

def init_move_matrix(rows, cols):
    
    matrix = []
    for idx_row in range(rows):
        row = []
        for idx_col in range(cols):
            row.append('.')
        matrix.append(row)

    matrix[rows-1][0] = 'H'

    return matrix, [rows-1, 0], [rows-1, 0]

def init_unique_matrix(rows, cols):

    matrix = []
    for idx_row in range(rows):
        row = []
        for idx_col in range(cols):
            row.append('.')
        matrix.append(row)

    matrix[rows-1][0] = '#'

    return matrix

def print_matrix(matrix):

    for idx_row in range(len(matrix)):

        for idx_col in range(len(matrix[idx_row])):
            print(matrix[idx_row][idx_col], end="")
        print("")


    return

def exec_movement(matrix, pos, tail, move):
    current_pos = pos
    tail_pos = tail

    move_func = {
        'R': move_right,
        'L': move_left,
        'U': move_up,
        'D': move_down
    }

    for i in range(int(move[1])):
        new_pos = move_func.get(move[0])(matrix, current_pos, tail_pos)
        diff_pos = [tail_pos[0] - new_pos[0], tail_pos[1] - new_pos[1]]

        if abs(diff_pos[0]) != 0 or abs(diff_pos[1]) != 0:            
            matrix[tail_pos[0]][tail_pos[1]] = "1"

        if abs(diff_pos[0]) > 1 or abs(diff_pos[1]) > 1:
            
            if abs(diff_pos[0]) > 0 or abs(diff_pos[1]) > 0:
                matrix[current_pos[0]][current_pos[1]] = "1"
                matrix[tail_pos[0]][tail_pos[1]] = "."
                unique_matrix[current_pos[0]][current_pos[1]] = "#"
            
            tail_pos = current_pos

        current_pos = new_pos

        print(move)
        #delay = timedelta(milliseconds=5)
        #time.sleep(delay.total_seconds())
        #os.system('cls')
        print_matrix(matrix)

    return current_pos, tail_pos

def check_matrix(matrix, pos, dest, tail_pos):
    tmp_list = []
    for idx in range(len(matrix[0])): tmp_list.append('.')

    tmp_list_u = []
    for idx in range(len(matrix[0])): tmp_list_u.append('.')

    if dest[0] < 0:
        matrix.insert(0, tmp_list)
        unique_matrix.insert(0, tmp_list_u)
        pos[0] += 1
        tail_pos[0] += 1

    elif dest[0] > len(matrix)-1:
        matrix.append(tmp_list)
        unique_matrix.append(tmp_list_u)
    
    if dest[1] < 0:
        for row in matrix: row.insert(0, '.')
        for row in unique_matrix: row.insert(0, '.')
        pos[1] += 1
        tail_pos[1] += 1

    elif dest[1] > len(matrix[0])-1:
        for row in matrix: row.append('.')
        for row in unique_matrix: row.append('.')

    return

def move_right(matrix, pos, tail_pos):
    dest = [pos[0], pos[1] + 1]
    check_matrix(matrix, pos, dest, tail_pos)

    if matrix[pos[0]][pos[1] + 1] == "1":
        matrix[pos[0]][pos[1] + 1] = "."
    matrix[pos[0]][pos[1]], matrix[pos[0]][pos[1] + 1] = matrix[pos[0]][pos[1] + 1], matrix[pos[0]][pos[1]]
    return [pos[0], pos[1] + 1]

def move_left(matrix, pos, tail_pos):
    dest = [pos[0], pos[1] - 1]
    check_matrix(matrix, pos, dest, tail_pos)

    if matrix[pos[0]][pos[1] - 1] == "1":
        matrix[pos[0]][pos[1] - 1] = "."
    matrix[pos[0]][pos[1]], matrix[pos[0]][pos[1] - 1] = matrix[pos[0]][pos[1] - 1], matrix[pos[0]][pos[1]]
    return [pos[0], pos[1] - 1]

def move_up(matrix, pos, tail_pos):
    dest = [pos[0] - 1, pos[1]]
    check_matrix(matrix, pos, dest, tail_pos)

    if matrix[pos[0] - 1][pos[1]] == "1":
        matrix[pos[0] - 1][pos[1]] = "."
    matrix[pos[0]][pos[1]], matrix[pos[0] - 1][pos[1]] = matrix[pos[0] - 1][pos[1]], matrix[pos[0]][pos[1]]
    return [pos[0] - 1, pos[1]]

def move_down(matrix, pos, tail_pos):
    dest = [pos[0] + 1, pos[1]]
    check_matrix(matrix, pos, dest, tail_pos)

    if matrix[pos[0] + 1][pos[1]] == "1":
        matrix[pos[0] + 1][pos[1]] = "."
    matrix[pos[0]][pos[1]], matrix[pos[0] + 1][pos[1]] = matrix[pos[0] + 1][pos[1]], matrix[pos[0]][pos[1]]
    return [pos[0] + 1, pos[1]]

if __name__=="__main__":

    move_splitter(move_list)
    #print(move_list)

    move_matrix, current_pos, tail_pos = init_move_matrix(5, 6)
    #print_matrix(move_matrix)
    unique_matrix = init_unique_matrix(5, 6)

    for move in move_list:
        print(" ")
        current_pos, tail_pos = exec_movement(move_matrix, current_pos, tail_pos, move)
        #print_matrix(move_matrix)

    print("Unique_pos:")
    #print_matrix(unique_matrix)

    count = 0
    for row in unique_matrix:
        for item in row:
            if item == '#':
                count += 1
    print(count)

    pass
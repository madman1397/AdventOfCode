import os

tree_list = list(open('Source\M_AOC2022_8.txt'))
blocked_list = []

for idx in range(len(tree_list)): 
    
    tree_list[idx], empty = tree_list[idx].split('\n')
    
    if idx == 0 or idx == (len(tree_list) - 1):
        continue
    blocked_list.append(tree_list[idx][1:(len(tree_list[idx]) - 1)])

#for idx in range(len(tree_list)): print(tree_list[idx])
#for idx in range(len(blocked_list)): print(blocked_list[idx])

def check_trees_blocked(idx_row, idx_col, tree_list):
    idx_row = int(idx_row)
    idx_col = int(idx_col)

    blocked_status = [False, False, False, False]

    # check left
    for idx in range(idx_col-1, -1, -1):
        if tree_list[idx_row][idx_col] <= tree_list[idx_row][idx]:
            blocked_status[0] = True
            break

    # check right
    for idx in range(idx_col+1, len(tree_list[idx_row])):
        if tree_list[idx_row][idx_col] <= tree_list[idx_row][idx]:
            blocked_status[1] = True
            break

    # check above
    for idx in range(idx_row-1, -1, -1):
        if tree_list[idx_row][idx_col] <= tree_list[idx][idx_col]:
            blocked_status[2] = True
            break

    # check below
    for idx in range(idx_row+1, len(tree_list)):
        if tree_list[idx_row][idx_col] <= tree_list[idx][idx_col]:
            blocked_status[3] = True
            break
    
    return (blocked_status[0] and blocked_status[1] and blocked_status[2] and blocked_status[3])
        
def check_trees_scenic(idx_row, idx_col, tree_list):
    idx_row = int(idx_row)
    idx_col = int(idx_col)

    scienic_val = [0, 0, 0, 0]

    # check left
    for idx in range(idx_col-1, -1, -1):
        scienic_val[0] += 1
        if tree_list[idx_row][idx_col] <= tree_list[idx_row][idx]:
            break
        
    # check right
    for idx in range(idx_col+1, len(tree_list[idx_row])):
        scienic_val[1] += 1
        if tree_list[idx_row][idx_col] <= tree_list[idx_row][idx]:
            break
            

    # check above
    for idx in range(idx_row-1, -1, -1):
        scienic_val[2] += 1
        if tree_list[idx_row][idx_col] <= tree_list[idx][idx_col]:
            break

    # check below
    for idx in range(idx_row+1, len(tree_list)):
        scienic_val[3] += 1
        if tree_list[idx_row][idx_col] <= tree_list[idx][idx_col]:
            break
    
    return (scienic_val[0] * scienic_val[1] * scienic_val[2] * scienic_val[3])

def check_row(idx_row, tree_list):
    blocked_count = 0
    unblocked_count = 0

    current_scenic = 0
    scenic_value = 0

    for idx_col in range(len(tree_list[idx_row])):

        if idx_col == 0 or idx_col == (len(tree_list[idx_row]) - 1):
            continue

        if check_trees_blocked(idx_row, idx_col, tree_list):
            blocked_count += 1
        else:
            unblocked_count += 1
        
        current_scenic = check_trees_scenic(idx_row, idx_col, tree_list)

        if(scenic_value < current_scenic):
            scenic_value = current_scenic

    return blocked_count, unblocked_count, scenic_value


if __name__=="__main__":
    sum_blocked = 0
    sum_unblocked = 0
    scenic_value = 0

    for idx_row in range(len(tree_list)):

        if idx_row == 0 or idx_row == (len(tree_list) - 1):
            continue

        blocked_count, unblocked_count, current_scenic = check_row(idx_row, tree_list)
        
        sum_blocked += blocked_count
        sum_unblocked += unblocked_count

        if(scenic_value < current_scenic):
            scenic_value = current_scenic

    sum_unblocked += len(tree_list) * 2
    sum_unblocked += (len(tree_list[0]) * 2) - 4

    print("Sum blocked: {}".format(sum_blocked))
    print("Sum unblocked: {}".format(sum_unblocked))
    print("Best scenic: {}".format(scenic_value))
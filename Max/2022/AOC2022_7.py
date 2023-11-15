import os

cmd_list = list(open('Source\M_AOC2022_7.txt').readlines())

# cmd definitions
CMD = "$"
CD = "cd"
CD_OUT = ".."
CD_HOME = "/"
LIST = "ls"
# folder / file definitions
FOLDER = "dir"

# ----------------------------------------------------------
for idx in range(len(cmd_list)): cmd_list[idx], empty = cmd_list[idx].split('\n')

current_folder = []
current_size = [0]
unused_space = 70000000 - 48008081
needed_space = 30000000 - 21991919

answer_sum = 0
del_folder = 0

# ----------------------------------------------------------
# ----------------------------------------------------------

def check_cmd(cmd_string):

    popped_size = 0

    if cmd_string[1] == CD:

        if cmd_string[2] == CD_HOME:
            current_folder.clear()
            current_folder.append(cmd_string[2])

        elif cmd_string[2] == CD_OUT:
            current_folder.pop()
            popped_size = current_size.pop()
            current_size[-1] += popped_size

        else:
            current_folder.append(cmd_string[2])
            current_size.append(0)
            
        print(current_folder)
        #print(current_size)

    elif item[1] == LIST:
        list_flag = True

    return popped_size
# ----------------------------------------------------------
def check_data(data_string):

    if data_string[0] == FOLDER:
        pass
    elif data_string[0] != FOLDER:
        current_size[-1] += int(data_string[0])

# ----------------------------------------------------------
# ----------------------------------------------------------

if __name__=="__main__":
    
    for i in range(len(cmd_list)):
        item = cmd_list[i].split()

        # ---- CD / LS ---
        if item[0] == CMD:
            next_sum = check_cmd(item)
            answer_sum += next_sum
            if next_sum >= needed_space:
                if (next_sum < del_folder and next_sum > 0) or (del_folder == 0):
                    del_folder = next_sum

        # ---- FOLDER / FILE ----
        elif item[0] != CMD:
            check_data(item)

    # ---- BACK TO HOME ----
    while len(current_size) > 1:
        check_cmd([CMD, CD, CD_OUT])
        #print(current_size)
        
    
    print(answer_sum)
    print(del_folder)

    print(current_size)
import os

com_list = list(open('Source\M_AOC2022_6.txt').readlines())

def check_marker_pos(com, mark_len):

    for i in range(len(com)):
        result = com[i:(i+mark_len)]
        if (len(result) > len(set(result))):
            continue
        else:
            print(result)
            return (i+mark_len)

    return 0

if __name__=="__main__":
    sum_marker_pos = 0
    for item in com_list:
        print(check_marker_pos(item, 4))
        print(check_marker_pos(item, 14))
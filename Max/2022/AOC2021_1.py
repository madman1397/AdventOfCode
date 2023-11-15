import os

src = open('Source\M_AOC2021_1.txt').readlines()
window_src = []

ic = 0
dc = 0
num1 = 0
num2 = 0

while num1 < (len(src) - 2):
    window_src.append(int(src[num1]) + int(src[num1 + 1]) + int(src[num1 + 2]))
    num1 += 1

while num2 < (len(window_src) - 1):
    if int(window_src[num2])<int(window_src[num2 + 1]):
        ic += 1
        num2 += 1
    else:
        dc += 1
        num2 += 1

print("Increases: {}".format(ic))
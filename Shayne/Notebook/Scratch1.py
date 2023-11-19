#1: Sum each file value to its parent dir (create dir variables, somehow dynamically.. OOP?)
#2: Iterate size values up the directories ultil it's summed at top dir '/'

crude = open("AdventOfCode\\Input\\Control\\2022\\Day_7.txt").readlines()
src = []

for ln in crude:
    src.append((ln.strip()).replace("$ ", ""))
#print(src)
chklist = []
cd = []
val = 0
for ln in src:
    
    if ln.split()[0] == "cd":
        if ln.split()[1] == "/":
            cd.clear()
            cd.append(ln.split()[1])
        elif ln.split()[1] == ".." and len(cd) > 1:
            cd.pop()
        else:
            cd.append(ln.split()[1])
    elif ln.split()[0] == "dir" or ln.split()[0] == "ls":
        print("placeholder")
    else:
        if ln.split()[0].isnumeric() == True and "".join(cd) not in chklist:
            print(str(val) + " + " + str(ln.split()[0]))
            val += int(ln.split()[0])
            print(val)
        else:
            chklist.append("".join(cd))
            val = 0
            print("passed")
    #print(cd)
    #print(ln)


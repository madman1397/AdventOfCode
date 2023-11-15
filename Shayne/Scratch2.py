crude = open("Input\Control\\2022\Day_7.txt").readlines()
src = []
#scrub data for unneeded values/white spaces
for ln in crude:
    src.append((ln.strip()).replace("$ ", ""))

#record directories that have already been totalled/prevent rechecks
chkdir = []
cd = []

#separate handling for files vs directories
for ln in src:
    #recognize/handle file listings
    if ln.split()[0].isnumeric() == True:
        print("Found file - " + str(ln))
    #recognize/handle directory listings
    elif ln.split()[0] == "dir":
        print("Found directory - " + str(ln))
    #recognize/handle input listings
    else:
        print("Input - " + str(ln))
        #Directory shift - Top/Back/Drill-in
        if ln.split()[0] == "cd":
            if ln.split()[1] == "/":
                cd.clear()
                cd.append(ln.split()[1])
            elif ln.split()[1] == "..":
                cd.pop()
            else:
                cd.append(ln.split()[1])
            print("New dir - " + str(cd))
            #Probably non-essential - flags for ls command
        else:
            print("Searching dir " + str(cd))
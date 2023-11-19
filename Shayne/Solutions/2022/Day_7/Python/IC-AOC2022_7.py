import os

sourceData = open("Input\Control\\2022\Day_7.txt").readlines()

#print(sourceData)
CDArray = []
lsDiscovery = []
TSum = 0
GSum = 0

def handleCMD(CDArray, ln):
    if ln[1] == 'cd':
            if ln[2] == '/':
                CDArray.clear()
                CDArray.append('/')
                print(CDArray)
                return CDArray
            elif ln[2] == '..':
                if len(CDArray) > 1:
                        CDArray.pop()
                        print(CDArray)
                        return CDArray
                else:pass
            else: 
                CDArray.append(ln[2])
                print(CDArray)
                return CDArray

#Handle command list
for ln in sourceData:
    ln = ln.strip().split()
    fullCD = ('/'.join(CDArray)+'/'+ln[1])
    #If is command:
    if ln[0] == '$':
        handleCMD(CDArray, ln)
    #If is return, NOTE: avoid dually counting files for total size
    else:
        if ln[0].isnumeric():
            if fullCD not in lsDiscovery:
                lsDiscovery.append(fullCD)
                print(ln)
                print('Counted')
                TSum += int(ln[0])
            else: 
                print(ln)
                print('Skipped')
            
print(TSum)
print(GSum)
        

#print(lsDiscovery)
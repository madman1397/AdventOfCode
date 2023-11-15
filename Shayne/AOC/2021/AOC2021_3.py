crude = open("Input\Shayne\\2021\Day_3.txt").readlines()
#----------------------------------------#
#scrub data into a more iterable state - write into list diagnosticReport
diagnosticReport = []
for line in crude:
    diagnosticReport.append(line.strip())
#----------------------------------------#
#Part 1 - ITERATE ALL BYTES; FIND MOST-(gamma) AND LEAST-(epsilon) COMMON BIT IN EACH POSITION
byteBin = []
for indices in diagnosticReport[0]:
    byteBin.append([])
byteIndex = 0
bitIndex = 0
gamma = []
epsilon = []

for byte in diagnosticReport:
    #print(byte)
    bitIndex = 0
    for bit in byte:
        #print(bit)
        byteBin[bitIndex].append(int(bit))
        bitIndex += 1

for bit in byteBin:
    if sum(bit) < len(bit)/2:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

gamma = ''.join(str(bit) for bit in gamma)
epsilon = ''.join(str(bit) for bit in epsilon)
#----------------------------------------#
#calculate power consumption (gamma * epsilon) in decimal format (base 2 to base 10)
print(int(gamma, 2)*int(epsilon, 2))
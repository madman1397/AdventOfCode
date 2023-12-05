import os
#THIS SECTION IS STRICTLY FOR DYNAMICALLY PULLING MY CORRESPONDING INPUT TXT AND IS BASED OFF MY DIRECTORY STRUCTURING, 
#THIS WILL LIKELY NOT BE APPLICABLE TO YOU UNLESS YOU USE THE SAME STRUCTURING.
Type = 'Control'
Year = __file__.split(os.sep)[-4:-3][0]
Day = __file__.split(os.sep)[-3:-2][0]
print('Advent Of Code',Year,Day)
Input = [line.strip() for line in open(os.path.join(os.sep.join(__file__.split(os.sep)[:-6]),'Input',Type,Year,Day+'.txt')).readlines()]
#print(Input) #TROUBLESHOOTING PRINTOUT; PRINTS FULL INPUT INTO A LIST WITH ONE LINE PER INDEX IN STRING FORM

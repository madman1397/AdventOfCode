#Define input, and strip data
Control = [line.strip() for line in open(str('/'.join(__file__.split('/')[:3])+'/Input/Control/'+'/'.join(__file__.split('/')[(len(__file__.split('/'))-4):(len(__file__.split('/'))-2)])+'.txt')).readlines()]
Unique = None
Input = Control
#Iterate data, remove non numeric characters, then concatenate only the first and last numerics on the line
Nums = [int(i[0]+i[-1]) for i in [''.join(filter(str.isdigit, i)) for i in Input]]
PartOne = sum(Nums)
print(PartOne)
# with open('day5/input1', 'r') as f:
#     for line in f.readlines():
#         # print(line.rstrip().rsplit())
#         print(line)

# Example input
# lst = [['Z','N'],['M','C','D'],['P']]

# Not sure how to convert input into list
lst = [['Q','F','M','R','L','W','C','V'],
       ['D','Q','L'],
       ['P','S','R','G','W','C','N','B'],
       ['L','C','D','H','B','Q','G'],
       ['V','G','L','F','Z','S'],
       ['D','G','N','P'],
       ['D','Z','P','V','F','C','W'],
       ['C','P','D','M','S'],
       ['Z','N','W','T','V','M','P','C']
]

# e.g., move 1 from 9 to 2
# move a from b to c
with open('day5/input2', 'r') as f:
    for line in f.readlines():
        ins = line.rstrip().rsplit()
        a,b,c = int(ins[1]),int(ins[3]),int(ins[5])
        for i in range(a):
            items = lst[b-1].pop()
            lst[c-1].append(items)

final_string = ''
for i in lst:
    final_string += str(i[-1:].pop())
print(final_string)
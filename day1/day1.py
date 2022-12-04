
with open('input', newline='\n') as f:
    output = [line.strip() for line in f.readlines()]
    
num = 0
lst = []
for i in output:
    if len(i) == 0:
        lst.append(num)
        # print("blank")
        num = 0
    else:
        num += int(i)
        # print(num)

print(max(lst))
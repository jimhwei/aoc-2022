pair_count = 0 

with open('day4/input') as f:
    for line in f.readlines():
        txt = line.strip().replace('-',' ').replace(',', ' ')
        lst = txt.split(' ')
        lst = [int(i) for i in lst]
        
        a = list(range(lst[0],lst[1]+1))
        b = list(range(lst[2],lst[3]+1))
        if (lst[2] in a or lst[3] in a) or (lst[0] in b or lst[1] in b): 
            pair_count += 1
            
print(pair_count)
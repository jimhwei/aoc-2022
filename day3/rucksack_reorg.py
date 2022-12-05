import string
values = dict()
for index, letter in enumerate(string.ascii_letters):
   values[letter] = index + 1

item_sum = 0

with open('day3/input', newline='\n') as f:
    for line in f.readlines():
        halfway = len(line.strip())//2
        str1 = line.strip()[:halfway]
        str2 = line.strip()[halfway:]
        # print(str1, str2)
        
        for letter in str1:
            if letter in str2:
                print(True)
                print (letter)
                item_sum += values[letter]
                break

print(item_sum)
# XYZ means you need to lose, draw, win
rps_dict = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
total_score = 0

with open('input', newline='\n') as f:
    for line in f.readlines():
        
        first_item = line.strip()[0]
        second_item = line.strip()[2]
        
        opp = rps_dict[first_item]
        me = rps_dict[second_item]

        # Tie
        if second_item == "Y": 
            score = 3 + opp
        
        # Lose
        elif second_item == "X": 
            if opp == 1:
                score = 3
            elif opp == 2:
                score = 1
            else: 
                score = 2
        
        # Win
        else: 
            if opp == 1:
                score = 2 + 6
            elif opp == 2:
                score = 3 + 6
            else: 
                score = 1 + 6
        
        total_score += score

print("total_score: ", total_score)
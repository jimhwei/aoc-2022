#A|X, B|Y, C|Z = Rock, Paper, Scissor 
rps_dict = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
total_score = 0
with open('day2/input', newline='\n') as f:
    for line in f.readlines():
        opp = rps_dict[line.strip()[0]]
        me = rps_dict[line.strip()[2]]

        victory_points = 0

        if opp == me:
            print("tie")
            victory_points = 3

        elif opp == 1:
            if me == 2:
                victory_points = 6
                print("win")
            else:
                print("lose")
        
        elif opp == 2:
            if me == 3:
                victory_points = 6        
                print("win")
            else:
                print("lose")
        else:
            if me == 1:
                victory_points = 6
                print("win")
            else:
                print("lose")

        score = me + victory_points
        total_score +=score

print("total_score: ", total_score)
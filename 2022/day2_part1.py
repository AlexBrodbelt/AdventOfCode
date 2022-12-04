oponent = ['A','B','C']
me = ['X','Y','Z']
scenarios = [f"{shape1} {shape2}" for shape1 in oponent for shape2 in me]
win, draw, loss = 6, 3, 0
rock, paper, scissors = 1, 2, 3
round_score = [draw, win, loss, loss, draw, win, win, loss, draw]
shape_score = [rock,paper,scissors]*3
overall_score = [x + y for x,y in zip(round_score, shape_score)]
scenario_scores = dict(zip(scenarios,overall_score))
total_score = 0
with open("day2_complex.txt", "r") as file:
    for round in file:
        round = round.strip("\n")
        total_score += scenario_scores[round]

print(total_score)



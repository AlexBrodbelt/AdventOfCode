oponent = ['A','B','C']
outcome = ['X','Y','Z']
scenarios = [f"{shape1} {shape2}" for shape1 in oponent for shape2 in outcome]
rock,paper,scissors = 1, 2, 3
win, draw, loss = 6, 3, 0
round_score = [loss, draw, win]*3
shape_score = [scissors,rock,paper,rock,paper,scissors,paper,scissors,rock]
overall_score = [x + y for x,y in zip(round_score, shape_score)]
scenario_scores = dict(zip(scenarios,overall_score))
total_score = 0
with open("day2_complex.txt", "r") as file:
    for round in file:
        round = round.strip("\n")
        total_score += scenario_scores[round]

print(total_score)
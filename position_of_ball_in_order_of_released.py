
# Given two arrays of H[] and B[] consisting of N and M integers respectively, denoting the diameter of holes and balls respectively. M number of balls are made to roll from A to B on a sloping surface with N holes, each having different depth as shown in the figure below:

# The task is to find the eventual position of each ball in the order of the ball released considering the following:

# A ball will fall into a hole if its diameter is less than or equal to the diameter of the hole.
# A hole Hi will become full if i numbers of balls fall into it.
# If a hole is full, then no more balls fall into it.
# A ball will reach B from A, if and only if it is not falling into any one of the holes.
# If a ball is in hole Pi, then its position is i. If a ball reached the bottom point B, then take its position as 0.

# Input: H[] = {21, 3, 6}, B[] = {20, 15, 5, 7, 10, 4, 2, 1, 3, 6, 8}
# Output: 1 0 3 0 0 3 3 2 2 0 0
# Explanation:
# Ball of diameter 20 will fall into the hole H1 and the hole H1 will become full.
# Balls with diameter 15, 7 and 10 will reach bottom, since the hole H1 is full and diameters of holes H2 and H3 are less than the diameters of the balls.
# Balls with diameters 5, 4 and 2 will fall into the hole H3.
# Ball with diameter 1 will fall into the hole H2 since the hole H3 is already full.
# Ball with diameter 3 will fall into hole H2.
# Balls with diameters 6, and 8 will reach the bottom point B.
# The position of ball 20 is 1 because it is in hole H1.
# Positions of ball 15, 7, 10, 3, 6, and 8 are 0 because they reached the bottom point B.
# Therefore, the balls with diameter 5, 4 and 2 are in the 3rd hole H3, the ball with diameter 1 and 3 are in the 2nd hole H2.

def holes_and_balls(holes, balls):
    ball_pos = []
    max_cnt_of_holes = []
    position_value = []

    for _ in range(1, len(holes) + 1):
        max_cnt_of_holes.append(_)
        position_value.append(_)
    print(max_cnt_of_holes)
    print(position_value)
    for i in range(len(balls)):
        for j in range(1, len(holes) + 1):
            if balls[i] <= holes[-j] and max_cnt_of_holes[-j] != 0:
                ball_pos.append(position_value[-j])
                max_cnt_of_holes[-j] -= 1
                break
            if j == len(holes):
                ball_pos.append(0)
                break
    return ball_pos


holes = [21, 3, 6]
print(holes)

balls = [20, 15, 5, 7, 10, 4, 2, 1, 3, 6, 8]
print(balls)

op = holes_and_balls(holes, balls)
print(*op, sep=', ')

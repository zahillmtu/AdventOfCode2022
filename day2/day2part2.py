# A is rock, B is paper, C is scissors
# X lose, Y draw, Z win
# 1 point for rock, 2 for paper, 3 for scissors
# 0 for loss, 3 for draw, 6 for win

def calculate_score(f):
    total_score = 0

    for line in f:
        opponent_hand = line.split(" ")[0]
        hand_result = line.split(" ")[1].strip()
        total_score += player_hand_score(opponent_hand, hand_result)
        total_score += player_score(hand_result)

    print(total_score)


def player_hand_score(opponent_hand, hand_result):
    return my_hand_points[ord(opponent_hand) - 65][ord(hand_result) - 88]


def player_score(hand_result):
    if hand_result == "X":
        return 0
    if hand_result == "Y":
        return 3
    if hand_result == "Z":
        return 6


# row is opponent hand, col is lose/draw/win
# value stored is point value of hand
my_hand_points = [
    [3, 1, 2],
    [1, 2, 3],
    [2, 3, 1]
]

calculate_score(open("input.txt", "r"))

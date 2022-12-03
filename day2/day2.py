# A/X is rock, B/Y is paper, C/Z is scissors
# 1 point for rock, 2 for paper, 3 for scissors
# 0 for loss, 3 for draw, 6 for win


def calculate_score(f):
    total_score = 0

    for line in f:
        opponent_hand = line.split(" ")[0]
        player_hand = line.split(" ")[1].strip()
        total_score += player_win_score(opponent_hand, player_hand)
        total_score += player_hand_score(player_hand)

    print("Total score " + str(total_score))


def player_win_score(opponent_hand, player_hand):
    return pointCombinations[ord(player_hand) - 88][ord(opponent_hand) - 65]


def player_hand_score(player_hand):
    if player_hand == "X":
        return 1
    if player_hand == "Y":
        return 2
    return 3


# row is player, col is opponent
pointCombinations = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]

calculate_score(open("input.txt", "r"))


Points_Red = 2
Points_Blue = 3

import sys
import random


#eval function to calculate the score
def calculate_game_score(rc, bc):
    current_score = rc * Points_Red + bc * Points_Blue
    score_difference = abs(rc - bc)
    random_factor = random.uniform(0.01, 0.1)  # Introduce some randomness within the range of 0.01 to 0.1
    game_score = current_score + score_difference + random_factor
    return game_score

def get_player_move(red_marbles, blue_marbles):
    while True:
        move = input("Enter your move (R/B): ").upper()
        if (move == 'R' and red_marbles > 0) or (move == 'B' and blue_marbles > 0):
            return move
        else:
            print("Invalid. Please choose a valid move.")

def alpha_beta_minimax(depth, alpha, beta, is_maximizing, rc, bc):
    if depth == 0 or rc == 0 or bc == 0:
        return None, calculate_game_score(rc, bc) if is_maximizing else calculate_game_score(rc, bc)

    best_action = None
    if is_maximizing:
        max_eval = float('-inf')
        for action in ['R', 'B']:
            if action == 'R' and rc > 0:
                new_red_count = rc - 1
                new_bc = bc
            elif action == 'B' and bc > 0:
                new_red_count = rc
                new_bc = bc - 1
            else:
                continue
            _, eval_score = alpha_beta_minimax(depth - 1, alpha, beta, False, new_red_count, new_bc)
            if eval_score > max_eval:
                max_eval = eval_score
                best_action = action
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return best_action, max_eval
    else:
        min_eval = float('inf')
        for action in ['R', 'B']:
            if action == 'R' and rc > 0:
                new_red_count = rc - 1
                new_bc = bc
            elif action == 'B' and bc > 0:
                new_red_count = rc
                new_bc = bc - 1
            else:
                continue
            _, eval_score = alpha_beta_minimax(depth - 1, alpha, beta, True, new_red_count, new_bc)
            if eval_score < min_eval:
                min_eval = eval_score
                best_action = action
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return best_action, min_eval



def main():
    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    game_version = sys.argv[3]
    starting_player = 'computer' if len(sys.argv) < 5 or sys.argv[4] == 'computer' else 'human'
    search_depth = int(sys.argv[5]) if len(sys.argv) >= 6 else None

    current_player = starting_player
    while num_red > 0 and num_blue > 0:
        print(f"Red marbles: {num_red}, Blue marbles: {num_blue}")

        if current_player == 'computer':
            move, _ = alpha_beta_minimax(search_depth, float('-inf'), float('inf'), True, num_red, num_blue)
            print(f"Computer chooses: {move}")
            if move == 'R':
                num_red -= 1
            else:
                num_blue -= 1
        else:
            move = get_player_move(num_red, num_blue)
            if move == 'R':
                num_red -= 1
            else:
                num_blue -= 1

        if game_version == 'misere':
            if num_blue == 0:
                winner = 'Human' if current_player == 'computer' else 'Computer'
                score = num_red * Points_Red + num_blue * Points_Blue
                print(f"{winner} wins with a score of {score}!")
                return
            elif num_red == 0:
                winner = 'Computer' if current_player == 'human' else 'Human'
                score = num_red * Points_Red + num_blue * Points_Blue
                print(f"{winner} wins with a score of {score}!")
                return
        else:
            if num_blue == 0:
                loser = 'Human' if current_player == 'computer' else 'Computer'
                score = num_red * Points_Red + num_blue * Points_Blue
                print(f"{loser} loses with a score of {score}!")
                return
            elif num_red == 0:
                loser = 'Computer' if current_player == 'human' else 'Human'
                score = num_red * Points_Red + num_blue * Points_Blue
                print(f"{loser} loses with a score of {score}!")
                return

        current_player = 'computer' if current_player == 'human' else 'human'

if __name__ == "__main__":
    main()

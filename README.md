# Red-Blue-Nim-AI
Red Blue Nim AI with Alpha Beta Pruning
Programming language - Python
Version - Python 3.10.11

The program results in a two-player game where each player takes their turn to remove one marble from a red or a blue pile. If on their turn, either pile is empty they win. Minimax algorithm and Alpha-Beta pruning are used to implement the game's computer moves.

Code Structure or how the code works:

The number of red and blue marbles is given as input to the evaluation function(calculate_game_score function), which calculates and gives an evaluation score, which is done by calculating the sum of red marbles multiplied by the constant Points_Red(2) and the blue marbles multiplied by the constant Points_blue(3). A random factor is used in this scenario to introduce some randomness between 0.01 and 0.1 in order to calculate the unpredictable conditions. The calculate_game_score function plays a crucial role in assessing and quantifying the state of a game. By combining the red and blue scores of players and introducing a random factor, the function creates an evaluation score that represents the current game state.

The get_player_move(red_marbles,blue_marbles) function takes in count the total number of red and blue marbles as input and in return provides the moves made by the player(say a human player) and also prompts the player to give their move (be it "R" or "B") and also performs a check if the player's move is a valid one or not.

The alpha_beta_minimax(depth, alpha, beta, is_maximizing, rc, bc) function is the implementation of the minimax algorithm along with alpha-beta pruning which accepts the input of the number of red and blue marbles, alpha-beta values, the depth of the search and finally the present player's status under is_maximizing variable. Also, along with the score, the function returns the best move for the current player.

The main function is the one which switches between the player(say a human player) and a computer. The count of how many piles of marbles( red and blue)are to be taken, the version to be played, the starting_player(human player or computer), and the depth are given as inputs to this function, which runs until all the marbles have been removed(i.e., either all red or vice versa). The winner or loser and the final scores are displayed at the end of the game.



To run the code, proceed to the directory consisting of this file in the respective terminal and go on with the following command:

python <file_name.py> <num_red> <num_blue> <game_version>  <starting_player> <depth>

where in - file_name.py = red_blue_nim_vxm2041.py
 	   num_red & num_blue = the total number of red and blue marbles you want to give as an input.
	   game_version = standard(Player loses if either pile is empty on their turn)
                          misere(Player wins if either pile is empty on their turn)
	   starting_player = computer-computer starts the game followed by human.
			      human  -human starts the game followed by the computer.

	   depth = the depth search for the minimax algorithm.


The complete code does not need any compilation,it has been tested and confirmed to run on a standard Python 3.10.11 installation.

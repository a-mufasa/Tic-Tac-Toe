# Tic-Tac-Toe

To run the game you need to cd into the main "Tic-tac-toe" folder. For minmax, run "python3 Minmax/Main.py" in the terminal. For alpha-beta pruning, run "python3 AlphaBeta/Main.py". To confirm you are in the running the correct algorithm, check the first line printed into the terminal (will state the algorithm being used).

After you run the program, it will ask you to choose if you will go first (1) or second (2). Regardless of choice, the human player uses the X and the AI uses O (I did this to make it easier to see what the AI's move is). Next, when it is your turn it prompt you to enter a position 1-9. The following diagram shows you you which position corresponds to which input choice:


| 1 || 2 || 3 |

| 4 || 5 || 6 |

| 7 || 8 || 9 |


I imported the math library for the 'inf' value, the random library for 'choice' so that we can choose a random start for when the AI goes first, and the time library to find runtime of algorithms. You can see the elapsed runtime for each call to the algorithm in the terminal.

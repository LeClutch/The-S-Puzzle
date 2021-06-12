# COMP472 Assignment 2

The goal of this Assignment is to use and analyze search algorithms to solve S-Puzzle.

We used 3 Search Algorithms by order of implementation:

- Iterative-Deepening
- Algorithm A*
- Depth-first

The algorithm takes input.txt which is 20 3x3 puzzles randomly generated.
Each search algorithm generates 2 output: Search path & Solution path.

PLEASE NOTE: THIS IMPLEMENTATION WILL ONLY OUTPUT 6 FILES!
If you would like to test our second heuristic function exchange the function names between lines 308 and 341

A timer is implemented so that if the program is not able to find the solution after 60 seconds, the output: No solution.

Analysis Implemented: A loop iterates over each line of "input.txt" to calculate the runtime for each algorithm and help us calculate the total length time 
of the solution paths and no solution paths.

# Expected Output:
0

Puzzle solved using iterative deepening search in 6.24821662902832 seconds.

Puzzle solved using A* search in 0.003999471664428711 seconds.

Done

1

Puzzle solved using iterative deepening search in 6.0850443840026855 seconds.

Puzzle solved using A* search in 0.019999265670776367 seconds.

Done

. 
.


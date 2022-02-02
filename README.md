# Wordle Solver

This program gives a complete algorithmic solution to the Wordle puzzle. The optimization is done by maximizing the information entropy gain for each guess over all posible five-letter word choices. It suggests the next guess based on the Wordle response until the cypher word is uniquely determined. From this perspective, the initial guess which provides the greatst information is "SOARE".

The algorithm was able to complete 100% of the full list of 2,315 Wordle answers in 7,945 total guesses for an average of 3.4320 guesses when using starting word "SALET". On hard mode, the algorithm completed 99.65% of words in 6 guesses or less, with an average of 3.6810 guesses per word.

WordleSolver.ipynb contains the solution algorithm.

WordleFunctions.ipynb contains auxillary functions for the program.

WordleSolverEvaluation.ipynb contains code for evaluating algorithm performance againt the complete list of Wordle answers.

wordle-answers-alphabetical.txt contains the list of 2,315 possible Wordle answers.

wordle-aceptable-guesses.txt contains an additional 10,657 words which are considered acceptable guesses.

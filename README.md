# Wordle

This program gives a complete algorithmic solution to the Wordle puzzle. The optimization is done by maximizing the information entropy gain at each step over all posible word choices. It recursively suggests the next responses based on the Wordle output until the cypher word is uniquely determined.

The program uses Donald Knuth's Graph Base of 5-letter words as a data set:

Donald E. Knuth. 1993. The Stanford GraphBase: a platform for combinatorial computing. Association for Computing Machinery, New York, NY, USA. https://www-cs-faculty.stanford.edu/~knuth/sgb.html

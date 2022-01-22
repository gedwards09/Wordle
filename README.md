# Wordle

This program gives a complete algorithmic solution to the Wordle puzzle. The optimization is done by maximizing the information entropy gain for each guess over all posible five-letter word choices. It suggests the next response based on the Wordle response until the cypher word is uniquely determined.

Wordle.ipynb contains the algoritm and and auxillary routines .

sgb-words.text contains Donald Knuth's Graph Base of 5-letter words, which is used as a data set:

Donald E. Knuth. 1993. The Stanford GraphBase: a platform for combinatorial computing. Association for Computing Machinery, New York, NY, USA. https://www-cs-faculty.stanford.edu/~knuth/sgb.html

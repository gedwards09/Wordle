import numpy as np
import pandas as pd

# Determines the Wordle response for a given guess and answer pair
#   answer: the hidden 5-letter code word
#   guess: the user supplies 5-letter guess word
#   returns a 5-letter Wordle signal (e.g. "GBYYB") with 'G' indicating a correct character in the correct position
#       'Y' indicating a correct character in the wrong position, and 'B' indicating an incorrect character
def wordle(answer,guess):
    sig=["B","B","B","B","B"]
    for i in range(5):
        if answer[i]==guess[i]:
            sig[i]="G"
    # create a count of remaining unidentified chars, ignoring the "G" positions
    dic={}
    for i in range(5):
        if sig[i]!="G":
            if answer[i] not in dic:
                dic[answer[i]]=1
            else:
                dic[answer[i]]+=1
    for i in range(5):
        if sig[i]!="G" and guess[i] in dic:
            if dic[guess[i]]>0:
                sig[i]="Y"
                dic[guess[i]]-=1
    ans=""
    for char in sig:
        ans+=char
    return ans

# determine if a word must be excluded when playing hard mode
# for a given guess and its response signal
#   word: potential 5-letter hidden code word
#   guess: the last 5-letter attempt
#   sig: the 5-letter Wordle signature returned by the guess, e.g. "GBYYB"
#   return: T/F if word can be considered in future guesses
def hardModeFilter(word,guess,sig):
    dic={}
    for i in range(5):
        # keep count of the "Y" chars that must appear in 
        # each possible guess
        if sig[i]=="Y":
            if guess[i] not in dic:
                dic[guess[i]]=1
            else:
                dic[guess[i]]+=1
    for i in range(5):
        if sig[i]=="G" and word[i]!=guess[i]:
            return False
        elif word[i] in dic:
            if dic[word[i]]>0:
                dic[word[i]]-=1
    for key in dic:
        if dic[key]>0:
            return False
    return True

# Determines the output Wordle cypher text for every possible hidden code word, given a chosen key
#   words: pandas series containing list of potential codewords to consider
#   key: guess word to apply to each word under consideration
#   returns 
def cypher(words,key):
    return words.apply(lambda x: wordle(x,key)).rename("cypher")

# computes the information entropy of a series of categorical values
#   series: a pandas series
#   returns float containing the numerical entropy of the categorical distribution
def entropy(series):
    dic={}
    n=len(series)
    for el in series:
        if el not in dic:
            dic[el]=1
        else:
            dic[el]+=1
    e=0
    for key in dic:
        p=dic[key]/n
        if p>0:
            e -= p*np.log(p)
    return e

# Determines the best next guess by choosing the word from the pool of all remaining guesses
# which maximizes information entropy after being applied to all possible answers.
# Applies a 'boost' to guesses which are possible answers to account for the 
# possiblity that they may give the correct answer immediately
#   possibleWords: pandas series containing all reamaining possible answers
#   allWords: pandas series containing all possible guesses, can be larger than the answer space
#   returns the 5-letter word which is the most informative guess
def nextWord(possibleWords,allWords):
    n=len(possibleWords)
    ans=""
    m=0
    for i in range(len(allWords)):
        word=allWords.iloc[i]
        series=cypher(possibleWords,word)
        e=entropy(series)
        # apply a boost for words which are still candiates
        # boost is positive since np.log(1-1/n)<0
        if i in possibleWords.index:
            e-=(1-1/n)*np.log(1-1/n)
        if e>m:
            m=e
            ans=word
    return ans
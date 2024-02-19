"""
Modify the sentence-generator program of Case Study 5.3 so that it inputs its
vocabulary from a set of text files at startup. The filenames are nouns.txt, verbs.
txt, articles.txt, and prepositions.txt. (Hint: Define a single new function,
getWords. This function should expect a filename as an argument. The function
should open an input file with this name, define a temporary list, read words
from the file, and add them to the list. The function should then convert the list
to a tuple and return this tuple. Call the function with an actual filename to initialize
each of the four variables for the vocabulary.)
"""

"""
in need to make 4 input statements, files are nouns.txt, verbs.txt, articles.txt and prepositions.txt
i need a new function (getWords) that takes a filename as an argument 

"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def getWords(listName):
    l =[]
    f = open(listName,'r')
    l.append(f.read().split())


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
    prepositionalPhrase()
def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()
def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
# The entry point for program execution
if __name__ == "__main__":
    main()
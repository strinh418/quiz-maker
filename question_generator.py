import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
# Link to tutorial: 
# https://medium.com/towards-artificial-intelligence/natural-language-processing-nlp-with-python-tutorial-for-beginners-1f54e610a1a0#7ec0
print("Please type one sentence.")
sentence = input()
tokenized_words = word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokenized_words)
print(tagged_words)

# How to extract a Noun Phrase from text
# Regex reminders
# ? - optional character
# * - 0 or more repetitions
grammar = "NP : {<DT>?<JJ>*<NN>}"

# Create a parser:
parser = nltk.RegexpParser(grammar)
output = parser.parse(tagged_words)
print(output)
output.draw()
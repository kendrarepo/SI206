# Name: Kendra Repo

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

print("\nSTART*******\n")

import nltk
import random
from nltk.book import *
from nltk import word_tokenize,sent_tokenize

debug = False # True

original_150 = text2[:150] 
original_150_formatted = ' '.join(original_150) # First 150 tokens in a readable format

print ('\nThe first 150 tokens of the original text:\n')
print (original_150_formatted)
print ('\n')

tokens = nltk.word_tokenize(original_150_formatted) # Divides string into lists of substrings
tagged_tokens = nltk.pos_tag(tokens) # Tagged list of tuples

if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","AV":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"AV":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
 		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
 	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
 		final_words.append(spaced(word))
 	else:
 		new_word = input("Please enter %s:\n" % (tagmap[tag]))
 		final_words.append(spaced(new_word))

print ("\nNew text: \n")
print ("".join(final_words))
print("\n\nEND*******")
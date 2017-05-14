import nltk
from nltk.corpus import wordnet as wn

# print(wn.synsets('glass'))
# print(wn.synset('glass.n.02').lemma_names())
# print(wn.synset('glass.n.02').definition())
# print(wn.synset('glass.n.01').definition())
# print(wn.synset('glass.n.02').part_meronyms())
# print(wn.synset('glass.n.02').part_holonyms())

print(wn.synsets('olympic_games'))
# print(wn.synset('glass.n.02').lemma_names())
print(wn.synset('window.n.02').definition())
# print(nltk.word_tokenize(wn.synset('coffee_table.n.01').definition()))
print(wn.synset('window.n.02').part_holonyms())
print(wn.synset('tree.n.01').part_meronyms())
print(wn.synset('olympic_games.n.01').definition())
print(wn.synset('olympic_games.n.01').member_meronyms())
print(wn.synset('tree.n.01').substance_meronyms())
# print(wn.synset('glass.n.02').part_holonyms())

# print(wn.synsets('towel'))
# print(wn.synset('towel.n.01').lemma_names())
# print(wn.synset('towel.v.01').lemma_names())
# print(wn.synset('towel.n.01').definition())
# print(wn.synset('towel.v.01').definition())
# 
# print(wn.synsets('chastity'))
# print(wn.synset('chastity.n.01').lemma_names())
# print(wn.synset('virtue.n.03').lemma_names())
# print(wn.synset('chastity.n.01').definition())
# print(wn.synset('virtue.n.03').definition())

help(wn)
# print(wn.synset('methamphetamine.n.01').definition())
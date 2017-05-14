import nltk
from nltk.corpus import gutenberg as gb
aust_pers = gb.words('austen-persuasion.txt')
print(len(set([w.lower() for w in aust_pers])))
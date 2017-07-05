import nltk
from nltk.corpus import gutenberg as gb

edge_parents = nltk.Text(gb.words('edgeworth-parents.txt'))
print(edge_parents.concordance('However'))
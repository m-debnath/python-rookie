import nltk
from nltk.corpus import webtext as wt

# print(wt.words('firefox.txt'))

fdist1 = nltk.FreqDist([w.lower() for w in wt.words('firefox.txt')])

print(fdist1.keys())
print(sorted(fdist1.values(), reverse=True))

print(list(fdist1.keys())[list(fdist1.values()).index(2428)])
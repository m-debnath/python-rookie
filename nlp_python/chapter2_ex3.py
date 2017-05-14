import nltk
from nltk.corpus import brown
from nltk.corpus import webtext

print(brown.fileids()[:5])
print(webtext.fileids()[:5])

print(webtext.words('overheard.txt')[:100])
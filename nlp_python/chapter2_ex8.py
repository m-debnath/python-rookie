import nltk
from nltk.corpus import names

print(names.fileids())

cfd = nltk.ConditionalFreqDist(
        (fileid, name.lower()[:1])
        for fileid in names.fileids()
        for name in names.words(fileid))
cfd.plot()
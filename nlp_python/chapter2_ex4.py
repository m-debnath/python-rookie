import nltk
from nltk.corpus import state_union

find_words = ['men', 'women', 'people']

cfd = nltk.ConditionalFreqDist(
        (word, fileid[:4])
        for fileid in state_union.fileids()
        for w in state_union.words(fileid)
        for word in find_words
        if w.lower().startswith(word))
cfd.plot()
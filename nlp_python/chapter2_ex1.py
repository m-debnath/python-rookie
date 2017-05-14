import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sent0 = "Homer Simpson is the best dad in the world."
sent1 = "The sound of some festival outside is horribly loud. A pigeon is trying to find a place for the night outside my window."
phrase = word_tokenize(sent0) + word_tokenize(sent1)
print(phrase)
for sent in sent_tokenize(sent1):
    print(sent)
print(phrase * 3)
find_words = ['the', 'outside', 'sound']
for find_word in find_words:
    for word in phrase:
        if find_word == word.lower():
             print(word, phrase.index(word))
cfd = nltk.ConditionalFreqDist(
             (word.lower(), phrase.index(word))
             for find_word in find_words
             for word in phrase if find_word == word.lower())
for condition in cfd.conditions():
    print(condition, cfd[condition].values())
#cfd.plot()
fdist = nltk.FreqDist(set([w.lower() for w in phrase]))
print(fdist.keys())
print(['please'] + phrase[-10:])

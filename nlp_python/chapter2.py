import nltk
nltk.corpus.gutenberg.fileids()

from nltk.corpus import gutenberg
emma = gutenberg.words('austen-emma.txt')
len(emma)

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)
    
macbeth_sents = gutenberg.sents('shakespeare-macbeth.txt')
longest_len = max([len(s) for s in macbeth_sents])
[s for s in macbeth_sents if len(s) == longest_len]

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:100])
    
from nltk.corpus import nps_chat
nps_chat.fileids()

for brown_cat in brown.categories():
    brown_text = brown.words(categories=brown_cat)
    fdist = nltk.FreqDist([w.lower() for w in brown_text])
    modals = ['can', 'could', 'may', 'might', 'must', 'shall', 'should', 'will', 'would']
    print('Category:', brown_cat)
    for m in modals:
        print(m + ':', str(fdist[m]) + '.  ', end='')
    print()

for brown_cat in brown.categories():
    brown_text = brown.words(categories=brown_cat)
    fdist = nltk.FreqDist([w.lower() for w in brown_text])
    whs = ['what', 'when', 'where', 'which', 'who', 'whom', 'whose', 'why', 'how']
    print('Category:', brown_cat + ',', 'Length:', len(brown_text))
    for wh in whs:
        print(wh + ':', str(fdist[wh]) + '.  ', end='')
    print()
    
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))

whs = ['what', 'when', 'where', 'which', 'who', 'whom', 'whose', 'why', 'how']
modals = ['can', 'could', 'may', 'might', 'must', 'shall', 'should', 'will', 'would']

cfd.tabulate(conditions=['news', 'editorial'], samples=modals)
cfd.tabulate(conditions=brown.categories(), samples=whs)

cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
        if w.lower().startswith(target))
cfd.plot()

f = open('C:\\Users\\Mukul\\Downloads\\gyb-1.0-windows\\gyb\\GYB-GMail-Backup-debnath.mukul@gmail.com\\2013\\6\\14\\13f40957bc873692.eml', 'r')

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'C:\\Users\\Mukul\\Downloads\\gyb-1.0-windows\\gyb\\GYB-GMail-Backup-debnath.mukul@gmail.com'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()

email_words = wordlists.words(fileids=wordlists.fileids())
email_chars = len(wordlists.raw(fileids=wordlists.fileids()))
email_words = len(wordlists.words(fileids=wordlists.fileids()))
email_sents = len(wordlists.sents(fileids=wordlists.fileids()))
email_vocab = sorted(set([w.lower() for w in wordlists.words(fileids=wordlists.fileids())]))

cfd = nltk.ConditionalFreqDist(
        (year, fileid[:4])
        for year in years
        for fileid in wordlists.fileids() if fileid[:4] in years)
cfd.plot()

cfd = nltk.ConditionalFreqDist(
        (genre, day)
        for day in days
        for genre in brown.categories()
        for word in brown.words(categories=genre) if word.lower().startswith(day))

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word + ' ', end = '')
        word = cfdist[word].max()
        
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfdist = nltk.ConditionalFreqDist(bigrams)
generate_model(cfdist, 'living')
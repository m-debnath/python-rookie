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
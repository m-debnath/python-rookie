from nltk.corpus import cmudict

entries = cmudict.entries()
print(len(entries))
for entry in entries[39943:39951]:
    print(entry)

for word, pron in entries:
    if(len(pron)) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2, end = ' ')
print()
#syllable = ['N', 'IH0', 'K', 'S']
syllable = ['AW1', 'N']
print([word for word, pron in entries if pron[-2:] == syllable])

print([w for w, pron in entries if pron[-1] == 'M' and w[-1].lower() == 'n'])

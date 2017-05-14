from nltk.corpus import cmudict

entries = cmudict.entries()

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])
print([w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']])

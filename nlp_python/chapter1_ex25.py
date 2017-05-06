sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

for token in sent:
    if token.startswith('sh'):
        print(token)
        
[w for w in sent if len(w) > 4]
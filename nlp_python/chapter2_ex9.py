import nltk
from nltk.corpus import brown as br
from nltk.corpus import stopwords as st

# print(br.fileids())
# 
# print(br.words('ca07')[10:100])
# 
# def lexical_diversity(words):
#     return len(words) / len(set(words))
# 
# print('ca01', lexical_diversity(br.words('ca01')))
# print('ca07', lexical_diversity(br.words('ca11')))
# 
# print('ca01', sorted(set([w.lower() for w in br.words('ca01') if len(w) > 7])))
# print('ca07', sorted(set([w.lower() for w in br.words('ca11') if len(w) > 7])))
# 
# print(nltk.Text(br.words('ca01')).concordance('Executive'))
# print(nltk.Text(br.words('ca11')).concordance('Executive'))
# 
# fdist1 = nltk.FreqDist(br.words('ca01'))
# fdist11 = nltk.FreqDist(br.words('ca11'))
# 
# print(fdist1.most_common(50))
# print(fdist11.most_common(50))

ca01 = br.words('ca01')
ca11 = br.words('ca11')

ca01_relev = set([w.lower() for w in ca01 for stop in st.words('english') if stop not in w])
ca11_relev = set([w.lower() for w in ca11 for stop in st.words('english') if stop not in w])

fdist01 = nltk.FreqDist(ca01_relev)
fdist11 = nltk.FreqDist(ca11_relev)

print(fdist01.most_common(50))
print(fdist11.most_common(50))
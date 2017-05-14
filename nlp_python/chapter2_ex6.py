import nltk
from nltk.corpus import swadesh

def trasnlate2en(lang, word):
    fr2en = swadesh.entries(['fr', 'en'])
    de2en = swadesh.entries(['de', 'en'])
    nl2en = swadesh.entries(['nl', 'en'])
    
    fr2en_trans = dict(fr2en)
    de2en_trans = dict(de2en)
    nl2en_trans = dict(nl2en)
    
    if lang == 'fr':
        return fr2en_trans[word]
    elif lang == 'de':
        return de2en_trans[word]
    elif lang == 'nl':
        return nl2en_trans[word]
    else:
        return ''
    
print(trasnlate2en('fr', 'chien'))
print(trasnlate2en('de', 'Hund'))
print(trasnlate2en('nl', 'hond'))
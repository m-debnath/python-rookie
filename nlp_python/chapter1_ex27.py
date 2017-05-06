def percent(word, text):
    fdist = FreqDist(text)
    return(100 * (fdist[word] / len(text)))
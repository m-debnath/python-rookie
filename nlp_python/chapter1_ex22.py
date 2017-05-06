dist45 = { fdist5[w] : w for w in set(text5) if len(w) == 4 }
sorted(dist45.items(), reverse=True)
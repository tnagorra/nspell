from lib import *

with open('tmp/dictionary/ne_NP.dic', 'r') as f:
    lst = set(f.read().split('\n'))
    lst = [x.split('/')[0] for x in lst]
    newlst = []
    for words in lst:
        for word in tokenize(words):
            if valid(word):
                newlst.append(word)
    dictionary = set(newlst)

with open('data/vocabulary-dictionary', 'w') as f:
    for word in sorted(dictionary, key=lambda x: length(x)):
        f.write(word+'\n')

#FIXME: one entry has (fdkaj, fdsakj, kdjsfal) pattern, remove that later

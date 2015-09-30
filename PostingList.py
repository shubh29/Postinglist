'''
Shubham Mahajan
'''

import nltk, os

# Dictionary - key: filename, value: file vocab
d = {}

# Read all .txt files in the current working directory
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        fOpen = open(file,'r')
        fRead = fOpen.read()
        d[file] = set([w.lower() for w in nltk.word_tokenize(fRead)])

# Gets the total vocab
vocab = set()
for key in d:
    vocab = vocab.union(d[key])
print('Vocabulary: ',vocab)

# Print the posting list
for w in sorted(vocab):
    print(w, end="")
    for key in d:
        for dw in d[key]:
            if(dw == w):
                print("  -->  ",key, end="")
    print()
    
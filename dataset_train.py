from cProfile import label
import json
from nltk_first_config import tokenize, stem, kumpulan_kata
import numpy as numped
with open('koleksi_ekspresi.json', 'r') as ekspresi:
    intents = json.load(ekspresi)

semua_kata = []
labels = []
ab = []

for intent in intents['intents']:
    label = intent['tag']
labels.append(label)
for pattern in intent['patterns']:
    w = tokenize(pattern)
    semua_kata.extend(w)
    ab.append((w, label))

    kata_terhiraukan = ['?', '!', '.', ',', '<', '>']
    semua_kata = [stem(w) for w in semua_kata if w not in kata_terhiraukan]
    semua_kata = sorted(set(semua_kata))
    labels = sorted(set(labels))
    labels = sorted(set(labels))
    print(labels)

    A_train = []
    B_train = []
    for (pattern_sentence, label) in ab:
        koleksi = kumpulan_kata(pattern_sentence, semua_kata)
        A_train.append(koleksi)

        tanda = labels.index(label)
        B_train.append(tanda) 

A_train = numped.array(A_train)
B_train = numped.array(B_train)

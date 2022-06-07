import nltk
import numpy as numped
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(kalimat):
    return nltk.word_tokenize(kalimat)

def stem(kata):
    return stemmer.stem(kata.lower())

def kumpulan_kata(tokenized_kalimat, semua_kata):
   

tokenized_kalimat = [stem(w) for w in tokenized_kalimat]

bag = numped.zeros(len(semua_kata), dtype=numped.float32)
for index, w in enumerate(semua_kata):
    if w in tokenized_kalimat:
        bag[index] = 1.0
# bahasa indo agak error ketika di stem, bahasa inggris full normal karena pake data dr inggirs speakers
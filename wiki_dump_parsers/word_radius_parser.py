# This parser will extract the following information for every page.
import pandas as pd
import numpy as np
import csv
from scipy.spatial.distance import cdist

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words= set(stopwords.words("english"))


columns=['title','words','radius']

# read word embeddings downloaded from https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
df=pd.read_csv('wiki.simple.vec', header=None, sep=' ', skiprows=1, quoting=csv.QUOTE_NONE, encoding='utf-8')
words=df[0].values
word2id=dict(zip(words,range(len(words))))
del df[0]
del df[301]
wordvec=df.values
del df

def parse(page):
    res=[]
    empty=True
    for rev in page:
        empty=False
        pass
    if empty:
        return res
    if rev.text is None:
        return res
    text=rev.text.lower()
    text=''.join([i if i.isalnum() else ' ' for i in text])
    text = [word for word in text.split() if word not in stop_words]
    y=np.array([wordvec[word2id[x.strip()]] for x in text if x.strip() in word2id])
    if len(y)==0:
        return res
    res.append(page.title)
    res.append(len(set(text)))
    centroid=np.mean(y,axis=0,keepdims=True)
    res.append(np.median(cdist(y,centroid)))
    return [res]

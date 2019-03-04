# This parser will extract the following information for every page.
from collections import Counter
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words= set(stopwords.words("english"))

columns=['title','word','freq']

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
    count=Counter(text)
    if len(count)==0:
        return res
    res=zip([page.title]*len(count),count.keys(),count.values())
    return res

# This parser will extract the following information for every page.
import pandas as pd
import numpy as np

columns=['title','policy','count']

# read policies
df=pd.read_csv('wiki_policies.tsv',sep='\t')
policy=df['Redirects'].tolist()
policy=[j.strip() for i in policy for j in i.split(',')]
policy=np.array(list(set(policy)))

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
    for i in policy:
        c=rev.text.count(i)
        if c>0:
            res.append([page.title, i, c])
    return res

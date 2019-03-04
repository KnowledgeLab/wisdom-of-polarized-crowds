# This is a template to parse wikipedia dumps. Plug in different parsers to extract different information.
import mwxml
import io
import pandas as pd
import numpy as np
import sys
import edit_info_parser as parser
from pathlib import Path

if sys.argv[3].upper()=='MAIN':
    namespace=0
elif sys.argv[3].upper()=='TALK':
    namespace=1
else:
    sys.exit("Wrong Namespace!")

title_file=sys.argv[2]

filename=sys.argv[1]
infile=filename[:-3]
test_file = Path(infile)
if not test_file.is_file():
    sys.exit()

outfile=filename[:-3]+'.tsv'

print("Processing {} pages in {}".format(sys.argv[3],infile))

# read titles
titles=set()
with io.open(title_file,'r',encoding='utf8') as f:
    for l in f:
        titles.add(l.strip('\n').replace(' ','').lower())

print("Load {} titles".format(len(titles)))

# clean titles
cleantitles=set()
dump = mwxml.Dump.from_file(open(infile))
for page in dump:
    if int(page.namespace) != namespace:
        continue
    if page.title.replace(' ','').lower() in titles:
        if page.redirect is None:
            cleantitles.add(page.title)
        else:
            cleantitles.add(page.redirect)

print("Found {} titles".format(len(cleantitles)))

# Parse the dump page by page
res=[]
dump = mwxml.Dump.from_file(open(infile))
for page in dump:
    if int(page.namespace) != namespace:
        continue
    if page.title in cleantitles:
        tmp=parser.parse(page)
        res.extend(tmp)

print("{} pages are assessed".format(len(res)))

df  = pd.DataFrame.from_records(res, columns=parser.columns)
df.to_csv(outfile, sep='\t', index=False, encoding='utf8')

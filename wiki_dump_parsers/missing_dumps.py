import glob
import sys

dumps=set()

with open(sys.argv[1]) as infile:
    for l in infile:
        dumps.add(l.strip())

files=glob.glob('*.tsv')
for f in files:
    dumps.discard(f.replace('.tsv','.7z'))

with open('missing_dumps.txt','w') as outfile:
    for f in dumps:
        outfile.write(f+'\n')

print(len(dumps))

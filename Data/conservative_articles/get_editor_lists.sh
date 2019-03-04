FILES=~/knowlab/wikipedia_projects/conservative_articles_full/*.7z
for f in $FILES

do
	7z e $f
	python edits.py ${f%.7z}
	rm ${f%.7z}
done

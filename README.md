# Wisdom of Polarized Crowds

This repo contains the code for the paper 

Citation to be added.

## Workflow
* Identify pages for politics, social issues and science titles. See the paper on how the corpra are identified.
* Download and parse the Wikipedia dump files for Wikipedia's complete snapshot (including all editing histories) on 20161201. (See [Wikipedia dump parsers](https://github.com/bill10/wiki_dump_parsers) for details.) In sum, 217 dump files are to be parsed; the following parsers are used.
  * attack_parser: extract page title, time, editor name, attack score, and aggressive score for each edit. It uses [wiki-detox](https://github.com/ewulczyn/wiki-detox) to assess the aggressive and attack scores. It relies on revision_differ.py and diff_match_patch.py (both are included) from [wikihadoop](https://github.com/whym/wikihadoop) to extract the difference between two snapshots of a page. Each line of the output corresponds to an edit. 
  * edit_info_parser: extract page title, time, editor name, and current page length for each edit. Each line of the output  corresponds to an edit.
  * policy_parser: extract page title, policy name, and number of mentions of the policy for each page. It uses a pre-compiled list of Wikipedia policies and guidelines (wiki_policies.tsv). Each line of the output corresponds to a (title, policy) combination.
  * quality_parser: assess the quality of each page. It uses [wikiclass](https://github.com/wikimedia/articlequality) and [revscoring](https://github.com/wikimedia/revscoring) to calculate the quality of each page. Each line of the output corresponds to page. 
  * tf_parser: calculate word frequncies for each page. It relies on the stopword dictionary from NLTK to remove stopwords. Each line of the output corresponds to a (page, word) combination.
  * word_radius_parser: extract page title, number of words, and radius of each page. It relies on the stopword dictionary from NLTK to remove stopwords. It uses the word embeddings from [fastText](https://fasttext.cc/docs/en/pretrained-vectors.html) to represent words as  numeric vectors; the radius of a page is then defined as the median distance from the words on the page to their centroid. Each line of the output corresponds to a page.
* Each parser will generate 217 TSV files containing the information extracted from the dumps. Tar those files into a tarball. The data_wrangling.ipynb will combine those files in the tarball and prepare the data for further analysis.
* Analysis is done in the analysis.ipynb notebook. 

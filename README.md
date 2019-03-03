# Wisdom of Polarized Crowds

This repo contains the code for the paper 

Citation to be added.

## Workflow
* Identify pages for politics, social issues and science titles. See the paper on how the corpra are identified.
* Download and parse the Wikipedia dump files for Wikipedia's complete snapshot (including all editing histories) on 20161201. (See [Wikipedia dump parsers](https://github.com/bill10/wiki_dump_parsers) for details.) In total, 217 dump files are to be parsed.
* Each parser will generate 217 TSV files containing the information extracted from the dumps. Tar those files into a tarball. The data_wrangling.ipynb will combine those files in the tarball and prepare the data for further analysis.
* Analysis is done in the analysis.ipynb notebook. 

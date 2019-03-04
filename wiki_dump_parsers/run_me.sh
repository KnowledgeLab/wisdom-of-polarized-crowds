#!/bin/bash
# This file will read in the necessary files, and submit the batch file to slurm for parsing
# Input:
#   1. a text file; one dump per line.
#   2. a text file; each line corresponds to a page title. (The words in a title are separated by space; case insensitive)
#   3. Namespace of wikipedia pages: TALK or MAIN (i.e., article)

mapfile -t FILES < $1

# get size of array
N=${#FILES[@]}
# now subtract 1 as we have to use zero-based indexing (first cell is 0)
N1=$(($N - 1))


# now submit to SLURM
if [ $N1 -ge 0 ]; then
    sbatch --array=0-$N1 submit.sh $1 $2 $3
fi

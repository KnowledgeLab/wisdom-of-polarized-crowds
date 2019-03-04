#!/bin/bash
#SBATCH --job-name=wikiparser
#SBATCH --output=%A_%a.out
#SBATCH --error=%A_%a.err
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=5:00:00
#SBATCH --mem=4000

# load python and packages
module add python
#export PYTHONPATH=path/to/custom/python/libraries:$PYTHONPATH

# grab out filename from the array
mapfile -t FILES < $1
FILENAME=${FILES[$SLURM_ARRAY_TASK_ID]}

# Run python script
python3 main.py $FILENAME $2 $3

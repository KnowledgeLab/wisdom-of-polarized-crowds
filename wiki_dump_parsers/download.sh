#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    wget https://dumps.wikimedia.org/enwiki/20180401/$line
    7z e $line
    rm $line
done < "$1"

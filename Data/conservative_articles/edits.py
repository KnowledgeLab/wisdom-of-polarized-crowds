import urllib
import xlrd
import csv
import xml.etree.ElementTree as ET
from   unidecode import *
import xlwt
import sys
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

def load_csv(filename):
    soups = []
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter='|')
    prev = 0
    for row in reversed(list(reader)):
	if row[2][1:-7] != '':
		curr = locale.atoi(row[2][1:-7])
		if abs(curr - prev) > 50: 
			soups.append(row[1])
		prev = curr
    return soups
    
def main(filename):
	out = open("../processed_data/processed_data/conservative_edits.txt", 'ab')
	wb = csv.writer(out)
	edits = load_csv(filename)
	wb.writerow([filename[11:-4]] + edits)
	out.close()
    
if __name__ == "__main__":
    main(sys.argv[1])

import codecs
import csv

filename = "//10.248.1.18/BPM Data/RDO Team Files/JP/M_VA_POL_MASK.csv"

with codecs.open(filename,"r",encoding='utf-8',errors='ignore') as f:
	reader = csv.reader(f)
	data = list(reader)
import os
import re
import glob
import numpy as np                                                                       
from numpy import sort      
import csv
from collections import namedtuple
from StringIO import StringIO

def concatenate1(regex):
	for f in glob.glob(regex):
		os.system("cat "+f+" >> out1.dat")

def concatenate2(regex):
	for f in glob.glob(regex):
		os.system("cat "+f+" >> out2.dat")

def convert_to_csv(inp, outp):
	with open(inp, 'r') as infile:
	    with open(outp, 'w') as outfile:
	        regex =re.compile(r'#')
	        for line in infile:
	            columns = line.strip().split()
	            if (regex.match(line) is None and line[0] != '$' and line[0] != '@' and line[0] != '*'):
	                outfile.write(",".join(columns)+"\n")

	            # if regex.match(line) is None or np.isnan(line) is False or np.isinf(line) is False:

def read_csv(file, columns, type_name = "Row"):
        try:
                row_type = namedtuple(type_name, columns)
        except ValueError:
                row_type = tuple
                rows = iter(csv.reader(file))
                header = rows.next()
                mapping = [header.index(x) for x in columns]
                for row in rows:
                        row = row_type(*[row[i] for i in mapping])
                        yield row

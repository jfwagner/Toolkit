#!/usr/bin/env python
# ******************************************************************************
# Code to replace strings in data files organized in columns
# ******************************************************************************
import sys

from util import replace_column

# Command line arguments
# ------------------------------------------------------------------------------ 
infile   = sys.argv[1]       # Name of the file you want to use
str_in   = sys.argv[2]       # Regular expression to match
col_in   = int(sys.argv[3])  # Column to apply regular expression
str_out  = sys.argv[4]       # What to replace
col_out  = int(sys.argv[5])  # and where

replace_column(infile, str_in, col_in, str_out, col_out)


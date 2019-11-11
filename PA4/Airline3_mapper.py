#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
    if words[50] != "''":
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print("{0}\t1".format(words[50]))

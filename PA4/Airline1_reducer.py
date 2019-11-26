#!/usr/bin/env python3

from operator import itemgetter
from collections import Counter
import sys

word = None
delays = Counter()
totals = Counter()
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    ID, delaydep, delayarr = word.split(',')

    try:
        totals[ID] += 1
        if delaydep == '1.00':
            delays[ID] += 1
        if delayarr == '1.00':
            delays[ID] += 1
    except:
        pass

for i in delays.keys():
    print('{0} {1}'.format(i, delays[i]/totals[i]))

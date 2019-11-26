#!/usr/bin/env python3

from operator import itemgetter
from collections import Counter
import sys

current_word = None
current_count = 0
word = None

counter = Counter()
num_of_route = Counter()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('|', 1)
    count = count.split()[0]
    # convert count (currently a string) to int
    try:
        count = float(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    counter[word] += count
    num_of_route[word] += 1
    '''
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print("{0}\t{1}".format(current_word, current_count))
        current_count = count
        current_word = word
  

# do not forget to output the last word if needed!
if current_word == word:
    print("{0}\t{1}".format(current_word, current_count))
  '''
for i in counter.keys():
    if int(counter[i]) > 5:
        print("{0}\t{1}".format(i, counter[i]/num_of_route[i]))
    

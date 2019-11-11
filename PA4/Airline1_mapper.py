#!/usr/bin/env python3

import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # print(words[6], words[34], words[45])
    print("{0},{1},{2}\t1".format(words[6].strip('"'), words[35], words[46]))

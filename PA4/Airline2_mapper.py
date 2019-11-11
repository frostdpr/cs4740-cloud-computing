#!/usr/bin/env python3

import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
    # print(words[6], words[34], words[45])
    #print("{0},{1},{2}\t1".format(words[6], type(words[35]), words[46]))
    try:
        airline = words[6].strip('"')
        if  airline == 'B6' or airline == 'F9' or airline == 'NK':
            print("{0} | {1}\t1".format((airline, words[14].strip('"') , words[24].strip('"')), words[45]))
    except:
        pass

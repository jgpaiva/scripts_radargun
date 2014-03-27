#!/usr/bin/env python

import sys
import re

usage = ''' script.py <file> <regex>+'''

if len(sys.argv) < 3:
    print(usage)
    sys.exit()

filename = sys.argv[1]
with open(filename, 'r') as f:
    file = f.read()
regexes = sys.argv[2:]

for line_number, line in enumerate(file.split("\n")):
    if len(line.strip()) == 0:
        continue
    elif line_number == 0:
        indexes = []
        items = []
        for item_index, item in enumerate(line.split(",")):
            for r in regexes:
                if re.search(r, item, re.I):
                    indexes.append(item_index)
                    items.append(item)
        indexes = set(indexes)
        print(",".join(map(str, items)))
    else:
        toprint = []
        for item_index, item in enumerate(line.split(",")):
            if item_index in indexes:
                item = float(item)
                toprint.append(item)
        print(",".join(map(lambda x: "{0:.2f}".format(x), toprint)))

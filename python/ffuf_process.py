#!/usr/bin/env python3


import csv
import sys
import os.path as  p

rawfile = sys.argv[1]
processed_file=sys.argv[2]

word_set = set()
writer = csv.writer(open(processed_file,'w'))



with open(rawfile,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        writer.writerow(next(csvreader))
        for row in csvreader:
            if row[4] is '401':
                writer.writerow(row)
                continue
            if row[6] not in word_set:
                word_set.add(row[6])
                writer.writerow(row)

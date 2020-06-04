#!/usr/bin/python3

import sys
import os.path as  p

filename = sys.argv[1]
basename = p.basename(filename)
basename = 'filtered_'+basename
dirname = p.dirname(filename)

outputfilename = p.join(dirname,basename)


def processing_line(d,line, count=10):
    delimeter = ","
    try:
        size_line1 = line.split("[")[2].strip()
        size_line2 = size_line1.split(delimeter)[1]
        size_line3 = size_line2.split(":")[1]
        size = size_line3.strip()

    except Exception as e:
        print(e)
        print("problematic line :"+line)
        print("problematic size line 1 :"+size_line1)
        print("problematic size line 2 :"+size_line2)
        print("problematic size line 3 :"+size_line3)
    size = int(size)
    if size in d :
        if len(d[size])< count:
            d[size].append(line)
    else:
        d[size] = [line]

def print_dict(d,output, count=10):
    for k,v in d.items():
        if len(v) < count:
            for line in v:
                output.write(line)


with open(outputfilename, 'w', encoding='utf-8') as output:
    with open(filename, 'r', encoding='utf-8') as input:
        lines = input.readlines()
        for line in lines:
            if  line.strip():
                if line.startswith("        /'___"):
                    try:
                        print_dict(d,output)
                    except NameError:
                        d = dict()

                if line[:2].isalpha() or line.startswith('[2K'):
                    processing_line(d,line)
                else:
                    output.write(line)

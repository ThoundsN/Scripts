#!/usr/bin/python3

import sys
filename = sys.argv[1]
outputfilename = sys.argv[2]


def processing_line(d,line, count=10):
    delimeter = ","
    size = line.split(delimeter)[1].split(":")[1].strip()
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

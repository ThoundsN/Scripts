#!/usr/bin/python3

import sys
filename = sys.argv[1]
outputfilename = "filtered_"+filename


def processing_line(d,line, count=500):
    delimeter = ","
    size = line.split(delimeter)[1].split(":")[1].strip()
    size = int(size)
    if size in d :
        if d[size].length() < count:
            d[size].append(line)
    else:
        d[size] = [line]

def print_dict(d,output, count=500):
    for k,v in d.items():
        if v.length() < count:
            for line in v:
                output.write(line)


with open(outputfilename, 'w', encoding='utf-8') as output:
    with open(filename, 'r', encoding='utf-8') as input:
        lines = input.readline()
        for line in lines:
            if line.startswith("        /'___\  /'___\ "):
                try:
                    print_dict(d,output)
                except NameError:
                    d = dict()
                output.write(line)

            if line[:1].isalpha():
                processing_line(d,line)
            else:
                output.write(line)

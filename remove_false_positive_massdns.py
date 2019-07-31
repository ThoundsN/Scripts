#!/usr/bin/python3

import sys

filename = sys.argv[1]

dns_dict = dict()

count = 12
bufsize = 100000
index=0


with open(filename,encoding='utf-8') as input:
    while True:
        lines = input.readlines(bufsize)
        index += bufsize
        # print(index)
        if not lines:
            break
        for row in input:
            # print(dns_dict)
            domain, recordtype, resource = row.split()
            # print(domain)
            # print(recordtype)
            # print(resource)
            if resource in dns_dict:
                if len(dns_dict[resource][0]) > count:
                    continue
                dns_dict[resource][0].append(domain)
            else:
                dns_dict[resource] = [[domain], recordtype]

for k,list in dns_dict.items():
    for row in list[0]:
            print(' '.join(map(str,[row,list[1],k])))

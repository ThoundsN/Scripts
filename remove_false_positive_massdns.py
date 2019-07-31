#!/usr/bin/python3

import sys

filename = sys.argv[1]

dns_dict = dict()

count = 12

with open(filename,encoding='utf-8') as input:
    for row in input:
        print(dns_dict)
        domain, recordtype, resource = row.split()
        print(domain)
        print(recordtype)
        print(resource)
        if resource in dns_dict:
            if len(dns_dict[resource[0]]) > count:
                continue
            dns_dict[resource[0]].append(domain)
        else:
            dns_dict[resource] = [[domain], recordtype]

for k,list in dns_dict.items():
    for row in list:
        for entity in row[0]:
            print(' '.join(map(str,[entity,row[1],k])))

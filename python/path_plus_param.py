#!/usr/bin/env python3

import argparse

import os
import sys
from iteration_utilities import grouper

count=7

def combine(path,params_turple):
    # print(args)
    params_list = list(params_turple)
    for item in range(0, len(params_list)):
      params_list[item] = params_list[item] +  '=FUZZ'

    query = '&'.join(params_list)
    url =   path + '?' + query 
    return url



# Create the parser
my_parser = argparse.ArgumentParser(description='Combine paths and params to generate new urls to fuzz')

my_parser.add_argument('-f',
                       '--params_files',
                        nargs='+',
                        required = True,
                        type=argparse.FileType('r'),
                       help='the location of input params file')

my_parser.add_argument('-p',
                       '--pathfiles',
                        nargs='+',
                        required = True,
                        type=argparse.FileType('r'),
                       help='the location of input path file ')

                    
args = my_parser.parse_args()

params_files = args.params_files
pathfiles = args.pathfiles

params_set = set()
paths_set = set()


for file in params_files:
    try:
        for param in file:
            params_set.add(param.strip())
    except Exception as e:
        pass

for file in pathfiles:
    for path in file:
        paths_set.add(path.strip())

params_grouped = list(grouper(params_set,count))

for domain_path in paths_set:
    for params_three in params_grouped:
        # parms_three is a turple 
        url = combine(domain_path,params_three)
        print(url)
# print(params_grouped)
# exit()


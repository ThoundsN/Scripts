#!/usr/bin/env python3


import argparse
import os
import sys
from iteration_utilities import grouper
import itertools
import re 
import glob 

def regex_line_hidden(line):
    a = re.findall(r'name=(\S+)',line)
    b = re.findall(r'value=(\S+)',line)
    # print(a) 
    # print(b) 

    # new = [a.replace('"','') for a in new_list]
    param = a[0].replace('"','')
    value = b[0].replace('"','')
    # print(param,value)
    return param,value

def parse_url(body):
    list = body.split('\n')
    path = list[0].split(' ')[1]
    host = list[1].split(': ')[1]
    url = 'https://' + host + path
    # print(url)
    return url

def combine_url(url,param,value):
    new_url = url+ '&' +param + '=' + value
    return new_url

def process_file(body):
    url = parse_url(body)
    param_value = {}
    for line in body.split('\n'):
        if 'type="hidden"' in line:
            param,value = regex_line_hidden(line)
            param_value[param]=value
    newurl_list = [combine_url(url,key,value) for key, value in param_value.items()]
    a_url = url 
    for key,value in param_value.items():
        a_url = combine_url(a_url,key,value)
    newurl_list.append(a_url)
    newurl_set = set(newurl_list)

    param_set =  set(param_value.keys())

    # print(newurl_set)
    # print(param_set)

    return newurl_set,param_set


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='Extract hidden parameters from response body and generate new url list ')

    my_parser.add_argument('-u',
                        '--url_file',
                            required = True,
                            type=argparse.FileType('a'),
                        help='the location of final_live_urls file')

    my_parser.add_argument('-p',
                        '--params_file',
                            required = True,
                            type=argparse.FileType('w'),
                        help='the location of output params file')                                

    my_parser.add_argument('-i',
                        '--input',
                            required = True,
                        help='the location of direcotry which contains response file from ffuf such as /ffuf/* ')

                        
    args = my_parser.parse_args()

    paths = glob.glob(os.path.abspath(args.input))

    # print(paths)
    global_newurls =set()
    global_params = set()
    for file in paths:
        with open(file,'r',encoding='unicode_escape') as f:
            body = f.read()
            if 'type="hidden"' in body:
                process_file(body)
                url_set,params_set = process_file(body)
                global_newurls = global_newurls.union(url_set)
                global_params = global_params.union(params_set)
    print(global_newurls)
    print(global_params)

    for element in global_params:
        args.params_file.write(element+'\n')
    
    for element in global_newurls:
        args.url_file.write(element+'\n')    
    




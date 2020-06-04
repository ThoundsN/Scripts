#!/usr/bin/env python3

import sys
import os.path as  p
import re 
from more_itertools import unique_everseen

# data sample 
#  /_Incapsula_Resource?SWJIYLWA=719d34d31c8e3a6e6fffd425f7e032f3&ns=1&cb=1768975551
#  /_Incapsula_Resource?SWJIYLWA=719d34d31c8e3a6e6fffd425f7e032f3&ns=2&cb=121104388
#  /belgium/blog/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.takeaway.com%2Fbelgium%
# 2Fblog%2Fbest-beoordeelde-bezorgrestaurants-december-2016%2F


def parse_pathandquery(string):
    string = string.strip()
    list = re.split('\?|&',string)
    # print('old     ')
    # print(list)
    # print('\n')
    for element in range(0, len(list)):
        if '=' in list[element]:
            list[element] = list[element].partition('=')[0]
        # print(list)
    # print('new      ')       
    # print(list)
    # print('\n')
    return list 

def segments_in_url(segments,url):
    for segment in segments:
        if segment not in url:
            return False
    return True

if __name__ == '__main__':


    path_query_file = sys.argv[1]
    urls_file=sys.argv[2]
    output = sys.argv[3]


    with open(path_query_file,'r', encoding="utf-8") as r:
        pathandquery_list = r.readlines()

    with open(urls_file,'r', encoding="utf-8") as rr:       
        urls = rr.readlines()

    processed_pathquerys = []
    for string in pathandquery_list:
        processed_pathquery = parse_pathandquery(string)
        processed_pathquerys.append(processed_pathquery)
        
    cleared = map(list,unique_everseen(map(tuple,processed_pathquerys)))
    processed_pathquerys = list(cleared)



    # for a in processed_pathquerys:
    #     print(a)
    
    # exit()



    unique_urls = set()

    for url in urls:
        for segments in processed_pathquerys:
            if segments_in_url(segments,url):
                unique_urls.add(url)
                processed_pathquerys.remove(segments)

    with open(output,'w', encoding="utf-8") as w:
        for url in unique_urls:
            w.write(url)
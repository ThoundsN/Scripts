#!/usr/bin/env python3


from urllib.parse import urlparse
import sys

input_path = sys.argv[1]
output_path=sys.argv[2]


if __name__ == '__main__':
    input =  open(input_path,'r')
    raw_urls = list(filter(None, input.read().splitlines()))
    domains = set()
    processed_urls=[]
    for url in raw_urls:
        result = urlparse(url)
        host = result.netloc
        protocol = result.scheme
        if protocol == 'http' :
            processed_urls.append(url)
            raw_urls.remove(url)
            domains.add(host)

    for url in raw_urls:
        result = urlparse(url)
        host = result.netloc
        if host not in domains:
            processed_urls.append(url)

    output = open(output_path,'w')
    for line in processed_urls:
        output.write(line)
        output.write('\n')
    output.close()
    input.close()

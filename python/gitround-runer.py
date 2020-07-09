#!/usr/bin/env python3

from invoke import run
import argparse
import datetime
import os

def run_githound(subdomain):
    global page_number
    global output_file
    cmd1 = " printf {} | git-hound --dig-files --dig-commits --many-results --pages {}    --regex-file ~/Wordlist/other/regex_githound.txt --threads 60  >> {}".format(subdomain,page_number,output_file)
    print(cmd1)
    print(datetime.datetime.now())
    result = run(cmd1, hide=True, warn=True)
    


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='A warpping 10 line script for git round ')

                    
    my_parser.add_argument('-o',
                    '--output_file',
                        required = True,
                    help='the location of output file of results ')

    my_parser.add_argument('-i',
                        '--input_subdomain_file',
                            required = True,
                        help='the location of subdomains file  ')

    my_parser.add_argument('-n',
                        '--page_number',
                            required = True,
                        help='Total pages to search for   ')                        

    args = my_parser.parse_args()
    page_number = args.page_number
    output_file = os.path.abspath(args.output_file)

    with open(output_file, 'w') as fp: 
        pass
    
    with open(args.input_subdomain_file,'r') as file:
        x = [l.rstrip("\n") for l in file]

    for subdomain in x:
        run_githound(subdomain)
        
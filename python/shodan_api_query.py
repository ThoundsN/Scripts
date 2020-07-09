#!/usr/bin/python3


import requests
import time
import os
import json
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

if len(sys.argv) < 3:
    print("""
    Usage :
        python3 {0} <query> <output_file>
    e.g. for favicon hash --
        python3 {0} http.favicon.hash:116323821 results_springboot.txt
    Use python3 for avoiding encoding issues, else add encode the title string errors
    How I Use it : python3 shodan_api_query.py "<query_here>" "<results_file_here>" | tee -a <another_minimal_output_file_here>
    """.format(__file__))
    sys.exit(1)

query = sys.argv[1] # http.favicon.hash:116323821
output_file = sys.argv[2] # results_springboot.txt

results = []
SHODAN_KEY = os.getenv("SHODAN_KEY", None)

if SHODAN_KEY is None:
    print("Export your shodan key as export SHODAN_KEY=<your_shodan_api_key>")
    sys.exit(1)

total, page_num = 1, 1
params = (
    ('key', SHODAN_KEY),
    ('query', query),
    ('page', str(page_num))
)
# Get total pages
try:
    response = requests.get('https://api.shodan.io/shodan/host/search', headers=headers, params=params)
    json_response = response.json()
    total = int(json_response['total']/100) # Since each api response contains 100 results
except Exception as e:
    print(e)
print("Total pages {}".format(total))

for page_num in range(0,total):
    params = (
        ('key', SHODAN_KEY),
        ('query', query),
        ('page', str(page_num))
    )
    try:
        print("Trying page_num {}".format(page_num))
        response = requests.get('https://api.shodan.io/shodan/host/search', headers=headers, params=params)
        matches = response.json()['matches']
        for result in matches:
            # Get the following
            # ip_str,hostnames,domains,timestamp,os,data,port
            final_result = {}
            try:
                final_result['http'] = result.get('http', '')
                final_result['ip_str'] = result.get('ip_str', '')
                final_result['hostnames'] = result.get('hostnames', '')
                final_result['domains'] = result.get('domains', '')
                final_result['timestamp'] = result.get('timestamp', '')
                final_result['os'] = result.get('os', '')
                final_result['data'] = result.get('data', '')
                final_result['port'] = result.get('port', '')
                print("host : {} title : {}".format(final_result.get('http').get('host'), final_result.get('http').get('title')))
            except Exception as e:
                print(e)
            finally:
                results.append(final_result)
        with open(output_file, 'w') as f:
            output = {"results": results}
            f.write(json.dumps(output))
        time.sleep(1)   # Since the API instructs so
    except Exception as e:
        print("Error in page_num : {}".format(page_num))
        print(e)
        pass
